-- For this challenge you need to create a SELECT statement, this select statement must have NULL handling, using COALESCE and NULLIF.

-- If no name is specified you must replace with [product name not found]

-- If no card_name is specified you must replace with [card name not found]

-- If no price is specified you must throw away the record, you must also filter the dataset by prices greater than 50.
-- eusales table schema

--     id
--     name
--     price
--     card_name
--     card_number
--     transaction_date

-- resultant table schema

--     id
--     name
--     price (greater than 50.00)
--     card_name
--     card_number
--     transaction_date

SELECT id,
COALESCE( NULLIF(name,'') , '[product name not found]' ) AS name,
price,
COALESCE( NULLIF(card_name,'') , '[card name not found]' ) AS card_name,
card_number, transaction_date
FROM eusales
WHERE price > 50;