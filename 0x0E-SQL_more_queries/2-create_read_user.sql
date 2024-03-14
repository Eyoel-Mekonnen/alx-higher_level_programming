-- script that creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- script that creates a new user with password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'usr_0d_2_pwd';
-- script that grants select privilige for the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
