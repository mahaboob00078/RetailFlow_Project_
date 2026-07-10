# Athena Cost Comparison

## Objective

Compare Athena query cost using an unpruned query (without partition filter) and a pruned query (with partition filter).

---

# Query 1 - Sample Data

```sql
SELECT * FROM customers
LIMIT 10;
```

Result

- Successfully returned customer records.

Data Scanned

- 508.03 KB

Screenshot

- Insert Screenshot 1 here.

---

# Query 2 - Unpruned Query

```sql
SELECT COUNT(*)
FROM orders;
```

Result

- 140002

Data Scanned

- <Write the bytes scanned shown by Athena



---

# Query 3 - Pruned Query

```sql
SELECT COUNT(*)
FROM orders
WHERE dt='2026-07-08';
```

Result

- <Write the result>

Data Scanned

- <Write the bytes scanned shown by Athena>

Screenshot
---

# Comparison

| Query | Partition Filter | Data Scanned |
|--------|------------------|--------------|
| Query 2 | No | <Bytes scanned> |
| Query 3 | Yes | <Bytes scanned> |

---

# Observation

The unpruned query scans all available partitions because no partition filter is used.

The pruned query scans only the required partition (`dt='2026-07-08'`), reducing the amount of data scanned when multiple partitions are present.

---

# Conclusion

Using partition pruning improves Athena query efficiency by reducing the amount of data scanned, which helps lower query costs and improve performance.