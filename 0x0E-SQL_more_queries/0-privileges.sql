--  lists all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost
-- SHOW GRANTS FOR 'user_0d_1'@'localhost', 'user_0d_2'@'localhost'
SELECT CONCAT('SHOW GRANTS FOR ''', user, '''@''localhost'';') AS SQLStatement
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2');
