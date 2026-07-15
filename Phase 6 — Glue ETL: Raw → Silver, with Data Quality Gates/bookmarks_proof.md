# Glue Job Bookmarks Proof

## Objective

Demonstrate that AWS Glue Job Bookmarks process only newly added data during subsequent runs.

## First Run

- Input:
  - orders_day1.json
  - order_items_day1.json
  - customers.csv
  - products.csv

Result:

- Glue Job Status: SUCCEEDED
- Curated data written to S3.
- All Day 1 records processed.

## Second Run

Additional files uploaded:

- orders_day2.json
- order_items_day2.json

Result:

- Glue Job Status: SUCCEEDED
- Job Bookmarks enabled.
- Only newly added Day 2 data was processed.
- Previously processed Day 1 data was skipped.

## Evidence

- Glue Job Run History
- Curated S3 output
- CloudWatch Logs
