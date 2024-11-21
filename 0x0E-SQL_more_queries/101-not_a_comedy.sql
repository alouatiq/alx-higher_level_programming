-- Script to list all shows that are not linked to the "Comedy" genre
-- Each record displays the show title
-- Results are sorted in ascending order by the show title

SELECT DISTINCT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_show_genres.show_id
    FROM tv_show_genres
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
