-- Top 3 cities' temperatures in July and August
SELECT city, AVG(temperature) AS avg_temp 
FROM temperatures 
WHERE month IN ('July', 'August') 
GROUP BY city 
ORDER BY avg_temp DESC 
LIMIT 3;
