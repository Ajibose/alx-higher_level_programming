-- Import in hbtn_0c_0 database this table dump
--  displays the max temperature of each state (ordered by State name).
-- SOURCE ./temperatures.sql
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`
LIMIT 3;
