-- You have access to two tables named top_half and bottom_half, as follows:

-- top_half schema

--     id
--     heads
--     arms

-- bottom_half schema

--     id
--     legs
--     tails

-- You must return a table with the format as follows:

-- output schema

--     id
--     heads
--     legs
--     arms
--     tails
--     species

-- The IDs on the tables match to make a full monster. For heads, arms, legs and tails you need to draw in the data from each table.

-- For the species, if the monster has more heads than arms, more tails than legs, or both, it is a 'BEAST' else it is a 'WEIRDO'. This needs to be captured in the species column.

-- All rows should be returned (10).

-- Tests require the use of CASE. Order by species.

SELECT T.id, heads, legs, arms, tails, 
CASE WHEN heads > arms OR tails > legs THEN 'BEAST' ELSE 'WEIRDO' END AS species
FROM top_half T
INNER JOIN bottom_half B ON T.id = B.id
ORDER BY species