-- Script to create the MySQL user 'user_0d_1' with all privileges
-- The user will have the username 'user_0d_1' and password 'user_0d_1_pwd'

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
