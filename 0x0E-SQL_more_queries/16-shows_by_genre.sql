-- Script to list all TV shows and their associated genres
-- Each record displays the show title and the genre name
-- Results are sorted in ascending order by the show title and genre name

SELECT tv_shows.title AS show_title, tv_genres.name AS genre_name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
