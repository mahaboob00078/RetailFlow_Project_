# Databricks notebook source

from pyspark import pipelines as dp
from pyspark.sql.functions import *

# Bronze to Silver

@dp.table(
    name="silver_orders",
    comment="Cleaned Orders Table"
)
def silver_orders():

    df = spark.read.table("retailflow.bronze.orders")

    return (
        df.dropDuplicates(["order_id"])
          .filter(col("order_id").isNotNull())
    )


# Silver to Gold

@dp.table(
    name="gold_order_summary",
    comment="Business Summary Table"
)
def gold_order_summary():

    df = spark.read.table("silver_orders")

    return (
        df.groupBy("status")
          .count()
    )
