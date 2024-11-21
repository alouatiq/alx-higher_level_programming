-- Script to list all genres and their cumulative ratings
-- Each record displays the genre name and the total rating sum
-- Results are sorted in descending order by the total rating

SELECT tv_genres.name AS genre, SUM(tv_show_ratings.rate) AS total_rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY total_rating DESC;
