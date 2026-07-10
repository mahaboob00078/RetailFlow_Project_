# RetailFlow Data Lake Architecture

## Overview

RetailFlow is an end-to-end AWS data lake project. The architecture follows the Medallion Architecture pattern, organizing data into Bronze (Raw), Silver (Curated), and Gold (Consumption) layers. Amazon S3 is used as the data lake, while AWS Glue and Amazon Athena are used for metadata management and analytics.

---

## Architecture Flow

Google Colab
        │
        ▼
Generate Retail Data
        │
        ▼
Python (Boto3)
        │
        ▼
Amazon S3
        │
        ├── raw (Bronze)
        ├── curated (Silver)
        └── consumption (Gold)
        │
        ▼
AWS Glue Crawler
        │
        ▼
Glue Data Catalog
        │
        ▼
Amazon Athena
        │
        ▼
SQL Analytics

---

## Bronze Layer (raw)

Purpose:
- Stores original source files.
- No transformations are applied.
- Acts as the source for all downstream processing.

Datasets:
- customers.csv
- products.csv
- orders_day1.json
- order_items_day1.json

Example:

raw/orders/dt=2026-07-08/orders_day1.json

---

## Silver Layer (curated)

Purpose:
- Stores cleaned and transformed data.
- Removes duplicates.
- Handles missing values.
- Standardizes schemas.

This layer will be populated using AWS Glue ETL jobs.

---

## Gold Layer (consumption)

Purpose:
- Stores business-ready datasets.
- Used for reporting and analytics.
- Queried by Amazon Athena.

Examples:
- Daily Sales
- Revenue by Category
- Customer Summary

---

## Partitioning Strategy

The raw layer is partitioned using the ingestion date.

Format:

raw/<dataset>/dt=YYYY-MM-DD/

Example:

raw/orders/dt=2026-07-08/orders_day1.json

Benefits:
- Faster query performance
- Lower Athena query costs
- Efficient incremental processing

---

## Naming Convention

Bucket:

retailflow-mahaboob-2026

Folders:

raw/
curated/
consumption/

Date Partition:

dt=YYYY-MM-DD

---

## Security

The S3 bucket is configured with:

- Bucket Versioning
- Server-Side Encryption (SSE-S3)
- Lifecycle Policy
- IAM-based access control

These settings help protect data, retain previous versions of objects, and optimize storage costs.

---

## Future Enhancements

- AWS Glue ETL Jobs
- Glue Data Catalog
- Amazon Athena
- Event-driven processing using S3 Event Notifications or EventBridge