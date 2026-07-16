-- Create Dimension Tables

CREATE TABLE dim_customer (...);

CREATE TABLE dim_product (...);

CREATE TABLE dim_date (...);

-- Create Fact Table

CREATE TABLE fact_order_items (...);

-- Create External Schema

CREATE EXTERNAL SCHEMA retailflow_consumption
FROM DATA CATALOG
DATABASE 'retailflow_raw'
IAM_ROLE 'arn:aws:iam::849287542814:role/RedshiftS3AccessRole'
CREATE EXTERNAL DATABASE IF NOT EXISTS;

-- Materialized View

CREATE MATERIALIZED VIEW mv_daily_revenue_by_category AS
SELECT
    order_date,
    category,
    total_revenue,
    total_orders
FROM retailflow_consumption.daily_revenue_by_category;
