-- For this challenge you need to create a simple query to display each unique clan with their total points and ranked by their total points.
-- people table schema

--     name
--     points
--     clan

-- You should then return a table that resembles below
-- select on

--     rank
--     clan
--     total_points
--     total_people

-- The query must rank each clan by their total_points, you must return each unqiue clan and if there is no clan name (i.e. it's an empty string) you must replace it with [no clan specified], you must sum the total_points for each clan and the total_people within that clan.

-- ##Note The data is loaded from the live leaderboard, this means values will change but also could cause the kata to time out retreiving the information.

SELECT ROW_NUMBER() OVER (ORDER BY SUM(points) DESC) AS rank,
CASE WHEN clan = '' OR clan IS NULL  THEN '[no clan specified]' ELSE clan END,
SUM(points) total_points, SUM(1) total_people
FROM people
GROUP BY clan
ORDER BY total_points DESC