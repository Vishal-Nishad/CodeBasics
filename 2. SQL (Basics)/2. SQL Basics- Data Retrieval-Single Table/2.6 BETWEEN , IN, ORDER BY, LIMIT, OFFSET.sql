SELECT * FROM movies;
SELECT * FROM movies WHERE imdb_rating>=9;
SELECT * FROM movies WHERE imdb_rating BETWEEN 6 AND 8;
SELECT * FROM movies WHERE release_year=2022 or release_year=2019 or release_year=2018;
SELECT * FROM movies WHERE release_year IN (2022,2019,2018);
SELECT * FROM movies WHERE imdb_rating is NULL;

SELECT *
FROM movies WHERE industry="Hollywood"
ORDER BY imdb_rating DESC LIMIT 8;

-- offset is use to skip top rows
SELECT *
FROM movies WHERE industry="Hollywood"
ORDER BY imdb_rating DESC LIMIT 8 OFFSET 4;