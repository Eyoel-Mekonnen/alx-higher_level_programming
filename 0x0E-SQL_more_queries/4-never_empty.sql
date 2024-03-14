-- create a table id_not_null
CREATE TABLE id_not_null IF NOT EXISTS(
	id INT DEFAULT 1, 
	name VARCHAR(256)
);
