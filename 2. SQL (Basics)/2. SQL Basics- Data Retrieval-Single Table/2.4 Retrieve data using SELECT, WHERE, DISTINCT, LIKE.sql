
USE moviesdb;
SELECT DISTINCT industry FROM movies;
SELECT * FROM movies WHERE industry = "Bollywood";
SELECT * FROM movies WHERE industry = "Hollywood";
SELECT * FROM movies WHERE title LIKE "%THOR%";
SELECT * FROM movies WHERE title LIKE "%AMERICA%";