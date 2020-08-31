-- Given a demographics table in the following format:

-- ** demographics table schema **

-- id
-- name
-- birthday
-- race
-- you need to return the same table where all text fields (name & race) are changed to the bit length of the string.

SELECT id, BIT_LENGTH(name) AS name, birthday, BIT_LENGTH(race) AS race
FROM demographics;