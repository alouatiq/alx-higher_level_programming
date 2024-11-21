
-- List all genres by their rating sum
SELECT tv_genres.name, SUM(rating) AS rating 
FROM tv_genres 
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
INNER JOIN tv_show_ratings ON tv_show_genres.tv_show_id = tv_show_ratings.tv_show_id 
GROUP BY tv_genres.name 
ORDER BY rating DESC;
