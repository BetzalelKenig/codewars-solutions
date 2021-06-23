-- For this challenge you need to create a UNION statement, there are two tables ussales and eusales the parent company tracks each sale at its respective location in each table, you must all filter the sale price so it only returns rows with a sale greater than 50.00. You have been tasked with combining that data for future analysis. Order by location (US before EU), then by id.
-- (us/eu)sales table schema

--     id
--     name
--     price
--     card_name
--     card_number
--     transaction_date

-- resultant table schema

--     location (EU for eusales and US for ussales)
--     id
--     name
--     price (greater than 50.00)
--     card_name
--     card_number
--     transaction_date

SELECT 'US' AS location, * 
FROM ussales WHERE price > 50
UNION ALL
SELECT 'EU' AS location, *
FROM eusales WHERE price > 50
ORDER BY location DESC, id