-- Script to list all shows and their genres
-- Includes shows without genres (NULL for genre)
-- Results are sorted in ascending order by show title and genre name

SELECT 
    tv_shows.title AS title, 
    tv_genres.name AS name
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN 
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY 
    tv_shows.title ASC, 
    tv_genres.name ASC;
