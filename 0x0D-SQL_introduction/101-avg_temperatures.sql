-- Calculate and display the average temperature (Fahrenheit) by city
-- Order the results by average temperature in descending order

SELECT 
    city, 
    ROUND(AVG(temperature), 4) AS avg_temp
FROM 
    temperatures
GROUP BY 
    city
ORDER BY 
    avg_temp DESC;
