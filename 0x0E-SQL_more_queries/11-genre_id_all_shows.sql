-- Script to list all shows and their linked genre IDs, including shows with no genres
-- Each record displays the show title and genre ID (NULL if no genre is linked)
-- Results are sorted by show title and genre ID in ascending order

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
