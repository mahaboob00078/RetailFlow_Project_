from pathlib import Path
from s3_client import S3Client

BUCKET_NAME = "retailflow-mahaboob-2026"

client = S3Client()

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "RetailFlow_Data"

files = [
    (
        str(DATA_DIR / "customers.csv"),
        "raw/customers/dt=2026-07-08/customers.csv"
    ),
    (
        str(DATA_DIR / "products.csv"),
        "raw/products/dt=2026-07-08/products.csv"
    ),
    (
        str(DATA_DIR / "orders_day1.json"),
        "raw/orders/dt=2026-07-08/orders_day1.json"
    ),
    (
        str(DATA_DIR / "order_items_day1.json"),
        "raw/order_items/dt=2026-07-08/order_items_day1.json"
    )
]

for local_file, s3_key in files:
    client.upload_file(local_file, BUCKET_NAME, s3_key)

print("Day 1 files uploaded successfully!")