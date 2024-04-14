-- lists all genres in the databse by their rating

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_shows
JOIN LEFT tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
