-- lists all ciites of california
USE hbtn_0d_usa
SELECT  *
FROM hbtn_0d_usa.states
WHERE name = "California"
ORDER BY name ASC;
