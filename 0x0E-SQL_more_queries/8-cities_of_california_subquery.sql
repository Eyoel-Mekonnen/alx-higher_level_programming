-- lists all ciites of california
USE hbtn_0d_usa
SELECT id, name
FROM cities
WHERE cities.state_id = (SELECT states.id FROM states.name = 'California')
ORDER BY cities.id ASC;
