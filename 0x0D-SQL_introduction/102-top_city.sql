-- Ensure the correct database is used
USE hbtn_0c_0;

-- Select the top 3 cities by average temperature for July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8) -- Filter for July (7) and August (8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
