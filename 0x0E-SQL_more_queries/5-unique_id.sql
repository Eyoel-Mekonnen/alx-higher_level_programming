-- create a new table that has unique value
CREATE TABLE IF NOT EXISTS uniqe_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
