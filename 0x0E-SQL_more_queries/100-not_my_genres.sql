
-- List all genres not linked to Dexter
SELECT name 
FROM tv_genres 
WHERE id NOT IN (
    SELECT genre_id 
    FROM tv_show_genres 
    INNER JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id 
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
