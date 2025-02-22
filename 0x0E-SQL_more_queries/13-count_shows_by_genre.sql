-- Script to list all genres and the number of shows linked to each
-- Each record displays the genre name and the count of shows
-- Results are sorted by the number of shows in descending order

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
