-- script that creats the MySQL server user "user_0d_1 
-- with all privileges, and the password user_0d_pwd.

DROP USER IF EXISTS 'user_0d_1'@'localhost';
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d__1_pwd';
GRANT ALL privileges ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;