-- Task

-- Given the information about sales in a store, calculate the total revenue for each day, month, year, and product.
-- Notes

--     The sales table stores only the dates for which any data has been recorded - the information about individual sales (what was sold, and when) is stored in the sales_details table instead
--     The sales_details table stores totals per product per date
--     Order the result by the product_name, year, month, day columns
--     We're interested only in the product-specific data, so you shouldn't return the total revenue from all sales

-- Input tables

-- ----------------------------------------
-- |    Table      |   Column   |  Type   |
-- |---------------+------------+---------|
-- | products      | id         | int     |
-- |               | name       | text    |
-- |               | price      | numeric |
-- |---------------+------------+---------|
-- | sales         | id         | int     |
-- |               | date       | date    |
-- |---------------+------------+---------|
-- | sales_details | id         | int     |
-- |               | sale_id    | int     |
-- |               | product_id | int     |
-- |               | count      | int     |
-- -----------------------------------------

-- Output table

-- --------------------------
-- |    Column    |  Type   |
-- |--------------+---------|
-- | product_name | text    |
-- | year         | int     |
-- | month        | int     |
-- | day          | int     |
-- | total        | numeric |
-- --------------------------

-- Example output

-- product_name | year | month | day | total
-- -------------+------+-------+-----+------
--  milk        | 2019 | 01    | 01  | 200
--  milk        | 2019 | 01    | 02  | 190
--  milk        | 2019 | 01    |     | 390
--  milk        | 2019 | 02    | 01  | 240
--  milk        | 2019 | 02    |     | 240
--  milk        | 2019 |       |     | 630
--  milk        |      |       |     | 630



SELECT p.name AS product_name,
  (EXTRACT(YEAR FROM  s.date))::INT AS year,
  (EXTRACT(MONTH FROM  s.date))::INT AS month,
  (EXTRACT(DAY FROM  s.date))::INT AS day,
  SUM(sd.count * p.price)::NUMERIC AS total
  
  FROM products AS p
   JOIN sales_details AS sd ON p.id = sd.product_id
   JOIN sales AS s ON sd.sale_id = s.id
  GROUP BY p.name, ROLLUP(year, month, day)
  ORDER BY p.name, year, month, day

