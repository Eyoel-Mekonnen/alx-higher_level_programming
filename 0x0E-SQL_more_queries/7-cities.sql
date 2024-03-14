-- create a Database htbn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the created database
USE hbtn_0d_usa
-- create a table that will reference to previous table
CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states (id)
);
