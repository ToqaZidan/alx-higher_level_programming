-- Script that crat a database and a user with privileges on it:

Drop DATABASE IF EXISTS hbtn_0d_2;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATe USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;