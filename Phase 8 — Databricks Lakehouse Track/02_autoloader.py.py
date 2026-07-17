# Databricks notebook source
# ==========================================================
# RetailFlow Project
# Phase 8 - Task 44
# Auto Loader (Directory Listing Mode)
# Bronze Clickstream Ingestion
# ==========================================================

from pyspark.sql.functions import *

# Read clickstream JSON files using Auto Loader
clickstream_df = (
    spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("cloudFiles.useNotifications", "false")
        .option(
            "cloudFiles.schemaLocation",
            "/Volumes/retailflow/bronze/clickstream_volume/schema"
        )
        .load("s3://retailflow-mahaboob-2026/clickstream/")
)

# Write streaming data into Bronze Delta table
(
    clickstream_df.writeStream
        .format("delta")
        .option(
            "checkpointLocation",
            "/Volumes/retailflow/bronze/clickstream_volume/checkpoint"
        )
        .trigger(availableNow=True)
        .toTable("retailflow.bronze.clickstream")
)

# Verify the data
spark.sql("""
SELECT *
FROM retailflow.bronze.clickstream
""").show()

# Verify the Bronze tables
spark.sql("""
SHOW TABLES IN retailflow.bronze
""").show()