# Redshift Performance Analysis

## Workload Management

Amazon Redshift Serverless uses Automatic Workload Management (Auto WLM).
Unlike provisioned Redshift clusters, manual WLM queues and Query Monitoring Rules are managed automatically by the service.

---

## Materialized View

Created Materialized View:

mv_daily_revenue_by_category

The materialized view improves query performance by storing precomputed aggregates.

---

## EXPLAIN Plan

Query:

SELECT
category,
SUM(total_revenue) AS revenue
FROM mv_daily_revenue_by_category
GROUP BY category
ORDER BY revenue DESC;

### Analysis

The query performs a Sequential Scan on the materialized view to retrieve the data.
It uses a HashAggregate operation to group records by category and compute the total revenue.
Finally, the results are sorted and merged before being returned to the leader node.
