-- COPY Commands

COPY dim_customer
FROM 's3://retailflow-mahaboob-2026/curated/customers/'
IAM_ROLE 'arn:aws:iam::849287542814:role/RedshiftS3AccessRole'
FORMAT AS PARQUET;

COPY dim_product
FROM 's3://retailflow-mahaboob-2026/curated/products/'
IAM_ROLE 'arn:aws:iam::849287542814:role/RedshiftS3AccessRole'
FORMAT AS PARQUET;

COPY fact_order_items
FROM 's3://retailflow-mahaboob-2026/curated/order_items/'
IAM_ROLE 'arn:aws:iam::849287542814:role/RedshiftS3AccessRole'
FORMAT AS PARQUET;

-- Verify

SELECT COUNT(*) FROM dim_customer;
SELECT COUNT(*) FROM dim_product;
SELECT COUNT(*) FROM fact_order_items;
