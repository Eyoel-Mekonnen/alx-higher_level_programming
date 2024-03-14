-- creates a dataabase named hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use that database
USE hbtn_0d_usa;
-- create a new table named states
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
