-- script that list all cities contained in the dtatabase
USE hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities, states
JOIN states ON cities.state_id = state.id
ORDER BY cities.id ASC;
