-- Create Masking Policy

CREATE MASKING POLICY test_mask
WITH (val VARCHAR)
USING ('****'::VARCHAR);

-- Attach Masking Policy

ATTACH MASKING POLICY test_mask
ON dim_customer(email)
TO PUBLIC;

-- Verify

SELECT
customer_id,
first_name,
email
FROM dim_customer
LIMIT 10;
