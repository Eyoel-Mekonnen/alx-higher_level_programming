-- lists all genres from hbtn_0d_tvshows and display the number of linked to each

SELECT tv_genre.name as genre, COUNT(tv_show_genre.genre_id) as 'number_of_shows'
FROM tv_genres
RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
