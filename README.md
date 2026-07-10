# RetailFlow Lakehouse Capstone

## Project Overview

RetailFlow is an AWS Data Engineering capstone project that demonstrates how to build an end-to-end cloud data platform. The project follows the Medallion Architecture (Bronze, Silver, and Gold) to transform raw retail data into business-ready datasets.

The project covers data generation, Amazon S3 data lake design, AWS Glue ETL, Amazon Athena, AWS Lake Formation, Amazon Redshift Serverless, and Databricks Lakehouse.

---

## Architecture

Google Colab
        │
        ▼
Synthetic Data Generation
        │
        ▼
Python (Boto3)
        │
        ▼
Amazon S3
(Bronze / Silver / Gold)
        │
        ▼
AWS Glue
        │
        ▼
Glue Data Catalog
        │
        ▼
Amazon Athena
        │
        ▼
Amazon Redshift Serverless

                │
                ▼

           Databricks
      Delta Lake & DLT

---

## Technologies Used

- Python
- Boto3
- Pandas
- NumPy
- Faker
- Matplotlib
- AWS S3
- AWS Glue
- AWS Athena
- AWS Lake Formation
- Amazon Redshift Serverless
- Databricks
- Delta Lake
- Git & GitHub

---

## Project Structure

```
retailflow-capstone/
│
├── RetailFlow_Data/
├── s3_ingest/
├── tests/
├── README.md
├── ARCHITECTURE.md
├── requirements.txt
├── .env.example
└── data_profile_report.md
```

---

## Project Phases

### Phase 0
- Environment Setup
- AWS Configuration
- Databricks Workspace

### Phase 1
- Synthetic Data Generation
- Data Profiling
- Data Visualization

### Phase 2
- Python Boto3 Ingestion Utility
- Logging
- Retry Logic
- S3 Upload

### Phase 3
- Amazon S3 Data Lake
- Bronze / Silver / Gold Structure
- Versioning
- Encryption
- Lifecycle Policy

### Phase 4
- AWS Glue Data Catalog
- Glue Crawlers
- Amazon Athena

### Phase 5
- AWS Lake Formation

### Phase 6
- AWS Glue ETL

### Phase 7
- Amazon Redshift Serverless

### Phase 8
- Databricks Lakehouse

### Phase 9
- Final Integration Report

---

## Features

- Synthetic retail dataset generation
- Three-layer data lake architecture
- Automated S3 ingestion using Boto3
- Data cataloging with AWS Glue
- SQL analytics using Athena
- Data governance with Lake Formation
- ETL pipelines with AWS Glue
- Business analytics using Redshift
- Lakehouse implementation using Databricks

---

## Author

Mahaboob Basha

AWS Data Engineering Capstone Project
