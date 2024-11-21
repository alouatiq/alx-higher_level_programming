-- Script to list all shows without any genre linked
-- Each record displays the show title and genre ID as NULL
-- Results are sorted in ascending order by show title

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
