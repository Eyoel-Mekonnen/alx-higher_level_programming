-- lists all genres in the databse by their rating

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
