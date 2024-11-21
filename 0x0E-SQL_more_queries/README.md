
# SQL Scripts for Advanced Queries and Table Management

This repository contains a collection of SQL scripts for managing MySQL databases, users, privileges, and advanced queries. Each script addresses a specific task or scenario related to database management or query execution.

## Files and Descriptions

| File Name                    | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `0-privileges.sql`           | Lists all privileges of MySQL users `user_0d_1` and `user_0d_2`.            |
| `1-create_user.sql`          | Creates a user `user_0d_1` with all privileges.                            |
| `2-create_read_user.sql`     | Creates a database `hbtn_0d_2` and a user `user_0d_2` with `SELECT` privilege. |
| `3-force_name.sql`           | Creates a table `force_name` with a `NOT NULL` constraint on the `name` column. |
| `4-never_empty.sql`          | Creates a table `id_not_null` with a default value for the `id` column.    |
| `5-unique_id.sql`            | Creates a table `unique_id` with a `UNIQUE` constraint on the `id` column. |
| `6-states.sql`               | Creates a table `states` with `id` as `PRIMARY KEY` and `AUTO_INCREMENT`.  |
| `7-cities.sql`               | Creates a table `cities` with a `FOREIGN KEY` referencing `states`.        |
| `8-cities_of_california_subquery.sql` | Lists all cities of California without using the `JOIN` keyword.       |
| `9-cities_by_state_join.sql` | Lists all cities with their states using `JOIN`.                           |
| `10-genre_id_by_show.sql`    | Lists all shows with at least one genre linked.                            |
| `11-genre_id_all_shows.sql`  | Lists all shows with their genres, showing `NULL` for shows without genres. |
| `12-no_genre.sql`            | Lists all shows without a genre linked.                                    |
| `13-count_shows_by_genre.sql`| Lists all genres and the number of shows linked to each.                   |
| `14-my_genres.sql`           | Lists all genres for the show `Dexter`.                                    |
| `15-comedy_only.sql`         | Lists all Comedy shows.                                                    |
| `16-shows_by_genre.sql`      | Lists all shows and their genres, showing `NULL` for shows without genres. |
| `100-not_my_genres.sql`      | Lists all genres not linked to the show `Dexter`.                          |
| `101-not_a_comedy.sql`       | Lists all shows without the genre `Comedy`.                                |
| `102-rating_shows.sql`       | Lists all shows by their rating sum.                                       |
| `103-rating_genres.sql`      | Lists all genres by their rating sum.                                      |
