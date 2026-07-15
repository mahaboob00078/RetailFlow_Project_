#retailflow_raw_to_curated

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

BUCKET = "retailflow-mahaboob-2026"

orders_path = f"s3://{BUCKET}/raw/orders/"
order_items_path = f"s3://{BUCKET}/raw/order_items/"
customers_path = f"s3://{BUCKET}/raw/customers/"
products_path = f"s3://{BUCKET}/raw/products/"

curated_path = f"s3://{BUCKET}/curated/"
quarantine_path = f"s3://{BUCKET}/quarantine/"

# Read Orders (JSON)
orders_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": [orders_path],
        "recurse": True
    },
    format="json"
)

# Read Order Items (JSON)
order_items_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": [order_items_path],
        "recurse": True
    },
    format="json"
)

# Read Customers (CSV)
# Read Customers (CSV)
customers_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": [customers_path],
        "recurse": True
    },
    format="csv",
    format_options={
        "withHeader": True
    }
)

# Read Products (CSV)
# Read Products (CSV)
# Read Products (CSV)
products_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": [products_path],
        "recurse": True
    },
    format="csv",
    format_options={
        "withHeader": True
    }
)

# Convert DynamicFrames to DataFrames

orders_df = orders_dyf.toDF()
order_items_df = order_items_dyf.toDF()
customers_df = customers_dyf.toDF()
products_df = products_dyf.toDF()

orders_df.printSchema()
order_items_df.printSchema()
customers_df.printSchema()
products_df.printSchema()

print("Orders Count:", orders_df.count())
print("Order Items Count:", order_items_df.count())
print("Customers Count:", customers_df.count())
print("Products Count:", products_df.count())

# Type Casting


orders_df = orders_df.withColumn("order_id", col("order_id").cast("int")) \
                     .withColumn("customer_id", col("customer_id").cast("int"))

order_items_df = order_items_df.withColumn("order_id", col("order_id").cast("int")) \
                               .withColumn("product_id", col("product_id").cast("int")) \
                               .withColumn("quantity", col("quantity").cast("int"))
                               
# Null Handling

orders_df = orders_df.na.drop(subset=["order_id", "customer_id"])

order_items_df = order_items_df.na.drop(subset=["order_id", "product_id"])

# Deduplication

orders_df = orders_df.dropDuplicates(["order_id"])

order_items_df = order_items_df.dropDuplicates(["order_id", "product_id"])

customers_df = customers_df.dropDuplicates(["customer_id"])

products_df = products_df.dropDuplicates(["product_id"])


# Convert DataFrames back to DynamicFrames

orders_dyf = DynamicFrame.fromDF(orders_df, glueContext, "orders_dyf")
order_items_dyf = DynamicFrame.fromDF(order_items_df, glueContext, "order_items_dyf")
customers_dyf = DynamicFrame.fromDF(customers_df, glueContext, "customers_dyf")
products_dyf = DynamicFrame.fromDF(products_df, glueContext, "products_dyf")


glueContext.write_dynamic_frame.from_options(
    frame=orders_dyf,
    connection_type="s3",
    connection_options={
        "path": curated_path + "orders/",
        "partitionKeys": ["status"]
    },
    format="glueparquet"
)



glueContext.write_dynamic_frame.from_options(
    frame=order_items_dyf,
    connection_type="s3",
    connection_options={
        "path": curated_path + "order_items/"
    },
    format="glueparquet"
)


glueContext.write_dynamic_frame.from_options(
    frame=customers_dyf,
    connection_type="s3",
    connection_options={
        "path": curated_path + "customers/"
    },
    format="glueparquet"
)


glueContext.write_dynamic_frame.from_options(
    frame=products_dyf,
    connection_type="s3",
    connection_options={
        "path": curated_path + "products/"
    },
    format="glueparquet"
)

job.commit()

#retailflow_data_quality

import sys

from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.transforms import SelectFromCollection

from pyspark.context import SparkContext
from pyspark.sql.functions import col

args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args["JOB_NAME"], args)

BUCKET = "retailflow-mahaboob-2026"
    
# Read Orders from Glue Catalog
orders_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": ["s3://retailflow-mahaboob-2026/raw/orders/"],
        "recurse": True
    },
    format="json"
)

# DQ Rules
ruleset = """
Rules = [
    IsComplete "order_id",
    IsComplete "customer_id",
    IsUnique "order_id"
]
"""

# Evaluate Data Quality
dq = EvaluateDataQuality().process_rows(
    frame=orders_dyf,
    ruleset=ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "RetailFlowOrdersDQ",
        "enableDataQualityCloudWatchMetrics": True,
        "enableDataQualityResultsPublishing": True,
        "resultsS3Prefix": f"s3://{BUCKET}/dq-results/"
    },
    additional_options={
        "performanceTuning.caching": "CACHE_NOTHING"
    }
)

# Extract row-level outcomes
rowLevelOutcomes = SelectFromCollection.apply(
    dfc=dq,
    key="rowLevelOutcomes",
    transformation_ctx="rowLevelOutcomes"
)

# Convert to Spark DataFrame
df = rowLevelOutcomes.toDF()

# Passed rows
passed_df = df.filter(
    col("DataQualityEvaluationResult") == "Passed"
)

# Failed rows
failed_df = df.filter(
    col("DataQualityEvaluationResult") == "Failed"
)

# Convert back to DynamicFrames
passed_dyf = DynamicFrame.fromDF(
    passed_df,
    glueContext,
    "passed_dyf"
)

failed_dyf = DynamicFrame.fromDF(
    failed_df,
    glueContext,
    "failed_dyf"
)

# Write passed rows
glueContext.write_dynamic_frame.from_options(
    frame=passed_dyf,
    connection_type="s3",
    connection_options={
        "path": f"s3://{BUCKET}/curated/orders_dq/"
    },
    format="glueparquet"
)

# Write failed rows
glueContext.write_dynamic_frame.from_options(
    frame=failed_dyf,
    connection_type="s3",
    connection_options={
        "path": f"s3://{BUCKET}/quarantine/orders/"
    },
    format="glueparquet"
)

job.commit()
