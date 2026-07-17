# Databricks notebook source

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Unity Catalog catalog and schema
catalog = "retailflow"
schema = "bronze"

# S3 curated location
base_path = "s3://retailflow-mahaboob-2026/curated/"

tables = [
    "customers",
    "products",
    "orders",
    "order_items",
    "orders_dq"
]

for table in tables:
    print(f"Creating Bronze table: {table}")

    df = spark.read.parquet(f"{base_path}{table}")

    (
        df.write
          .format("delta")
          .mode("overwrite")
          .saveAsTable(f"{catalog}.{schema}.{table}")
    )

print("Bronze layer creation completed successfully.")

# Verify tables
spark.sql("SHOW TABLES IN retailflow.bronze").show(truncate=False)
