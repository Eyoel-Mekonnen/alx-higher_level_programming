-- script that lists all shows by their rating

SELECT tv_shows.title, SUM(tv_shows_rating.rate) AS 'rating'
FROM tv_shows
JOIN tv_show_rating ON tv_show_rating.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
