-- Import in hbtn_0c_0 database this table dump
-- displays the average temperature (Fahrenheit) by city
-- ordered by temperature (descending).
-- SOURCE ./temperatures.sql
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
