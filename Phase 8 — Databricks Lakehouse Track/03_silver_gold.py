# ==========================================================
# RetailFlow Capstone
# Phase 8 - Task 45
# Silver & Gold Delta Tables
# ==========================================================

from pyspark.sql.functions import count

# ==========================================================
# Create Silver and Gold Schemas
# ==========================================================

spark.sql("""
CREATE SCHEMA IF NOT EXISTS retailflow.silver
""")

spark.sql("""
CREATE SCHEMA IF NOT EXISTS retailflow.gold
""")

# ==========================================================
# Read Bronze Orders Table
# ==========================================================

orders_df = spark.table("retailflow.bronze.orders")

# ==========================================================
# Silver Layer
# Remove duplicate records
# ==========================================================

orders_silver = orders_df.dropDuplicates()

# ==========================================================
# Write Silver Delta Table
# Enable Change Data Feed (CDF)
# ==========================================================

(
    orders_silver.write
        .format("delta")
        .mode("overwrite")
        .option("delta.enableChangeDataFeed", "true")
        .saveAsTable("retailflow.silver.orders")
)

# ==========================================================
# Read Silver Table
# ==========================================================

silver_orders = spark.table("retailflow.silver.orders")

# ==========================================================
# Gold Layer
# Business Aggregation
# ==========================================================

gold_orders = (
    silver_orders
        .groupBy("status")
        .agg(
            count("*").alias("total_orders")
        )
)

# ==========================================================
# Write Gold Delta Table
# ==========================================================

(
    gold_orders.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable("retailflow.gold.order_summary")
)

# ==========================================================
# Verify Gold Table
# ==========================================================

spark.sql("""
SELECT *
FROM retailflow.gold.order_summary
""").show()

# ==========================================================
# Verify Silver Tables
# ==========================================================

spark.sql("""
SHOW TABLES IN retailflow.silver
""").show()

# ==========================================================
# Verify Gold Tables
# ==========================================================

spark.sql("""
SHOW TABLES IN retailflow.gold
""").show()