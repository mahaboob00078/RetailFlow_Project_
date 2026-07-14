# Lake Formation Governance

## Objective

Implemented AWS Lake Formation LF-Tag-based governance to protect sensitive customer data using fine-grained column-level access control.

---

## LF-Tags Created

### sensitivity
- Public
- Confidential
- PII

### department
- analytics
- engineering

---

## LF-Tag Assignments

### Database
Database: retailflow_raw

LF-Tag:
- sensitivity = Confidential

### Table
Table: customers

LF-Tag:
- sensitivity = Confidential

### Column-Level Tags

| Column | LF-Tag |
|---------|---------|
| customer_id | Confidential |
| first_name | Confidential |
| last_name | Confidential |
| email | PII |
| phone | Confidential |
| city | Confidential |
| state | Confidential |
| country | Confidential |
| signup_date | Confidential |
| dt | Confidential |

---

## IAM Personas

### data_analyst

IAM Policies
- AmazonAthenaFullAccess
- AWSGlueConsoleFullAccess
- AthenaQueryResultsS3Access

LF-Tag Permissions
- Confidential

Database Permission
- Describe

Table Permissions
- Describe
- Select

---

### data_engineer

IAM Policies
- AmazonAthenaFullAccess
- AWSGlueConsoleFullAccess
- AWSLakeFormationDataAdmin
- AthenaQueryResultsS3Access

LF-Tag Permissions
- Confidential
- PII

Database Permission
- Describe

Table Permissions
- Describe
- Select

---

## Verification

### data_analyst

Query:

```sql
SELECT * FROM customers LIMIT 10;
```

Result:
- email column is NOT visible.

---

### data_engineer

Query:

```sql
SELECT * FROM customers LIMIT 10;
```

Result:
- All columns including email are visible.

---

## Conclusion

Lake Formation LF-Tag-based governance was successfully implemented.

The data_analyst persona can access only non-PII customer information, while the data_engineer persona can access both Confidential and PII data. This demonstrates successful implementation of column-level security using AWS Lake Formation.