# RetailFlow Data Profile Report

## Overview

This report summarizes the profiling results of the RetailFlow synthetic datasets generated using Python, Faker, NumPy, and Pandas. The objective is to identify data quality issues before ingestion into the AWS data lake.

---

# Datasets Profiled

- customers.csv
- products.csv
- orders_day1.json
- order_items_day1.json
- orders_day2.json
- order_items_day2.json
- clickstream_day1.json
- clickstream_day2.json

---

# Data Quality Summary

## customers.csv

Observations

- Contains customer information.
- Some email addresses are null or malformed.
- Duplicate customer IDs are present to simulate dirty data.
- Customer IDs are unique except for intentionally injected duplicates.

Issues Found

- Null email values
- Malformed email addresses
- Duplicate customer_id values

---

## products.csv

Observations

- Product information is complete.
- Product categories are well distributed.
- No major missing values detected.

Issues Found

- No significant issues.

---

## orders_day1.json

Observations

- Contains order header information.
- Includes order timestamp, customer ID, status, and region.

Issues Found

- No major issues.

---

## order_items_day1.json

Observations

- Contains order line details.
- Includes quantity, unit price, and line total.

Issues Found

- A few product_id values do not exist in products.csv to simulate referential integrity failures.
- A few zero or negative quantity values were intentionally introduced.

---

## orders_day2.json

Observations

- Incremental batch of order headers.
- Introduces a new column:

discount_code

Purpose

- Simulates schema evolution.

---

## order_items_day2.json

Observations

- Incremental order items.
- Continues day2 data.

Issues Found

- Same referential integrity issues as day1.

---

## clickstream_day1.json

Observations

- Contains website clickstream events.
- Used later for Databricks Auto Loader.

Issues Found

- No major issues.

---

## clickstream_day2.json

Observations

- Incremental clickstream events.

Issues Found

- No major issues.

---

# Data Profiling Summary

The following checks were performed using Pandas:

- Null value analysis
- Data type summary
- Duplicate record detection
- Value range validation

---

# Charts Generated

The following visualizations were created:

1. Order Volume by Day
2. Revenue Distribution
3. Top 10 Categories by Revenue
4. Null Rate Heatmap

---

# Key Findings

- Null email values exist in customers.csv.
- Duplicate customer IDs were intentionally introduced.
- Some order_items reference invalid product IDs.
- A few quantity values are zero or negative.
- Day2 introduces schema evolution using the discount_code column.
- Dataset is suitable for demonstrating data cleansing, schema evolution, and data quality validation in AWS Glue.

---

# Conclusion

The generated RetailFlow dataset successfully simulates real-world data quality issues, including missing values, duplicates, referential integrity failures, and schema evolution. These datasets will be ingested into Amazon S3 and processed through AWS Glue, Athena, Redshift, and Databricks in the subsequent phases of the capstone project.