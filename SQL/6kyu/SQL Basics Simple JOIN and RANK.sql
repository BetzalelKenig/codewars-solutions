-- For this challenge you need to create a simple SELECT statement that will return all columns from the people table, and join to the sales table so that you can return the COUNT of all sales and RANK each person by their sale_count.
-- people table schema

--     id
--     name

-- sales table schema

--     id
--     people_id
--     sale
--     price

-- You should return all people fields as well as the sale count as "sale_count" and the rank as "sale_rank".

WITH S AS (
SELECT people_id, COUNT(sale) sale_count, SUM(price) sum
FROM sales
GROUP BY people_id
)
SELECT people.*, S.sale_count, S.sum sale_rank FROM people
INNER JOIN S
ON people.id = S.people_id
ORDER BY S.sum