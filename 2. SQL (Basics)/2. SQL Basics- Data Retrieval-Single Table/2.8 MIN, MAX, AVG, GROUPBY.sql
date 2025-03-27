SELECT * FROM movies;
SELECT MIN(imdb_rating) as min_rating,
	   MAX(imdb_rating) as max_rating,
ROUND(AVG(imdb_rating),2) as avg_rating 
FROM movies WHERE studio="Marvel Studios";

SELECT industry,COUNT(*) as total
FROM movies
GROUP BY industry;

SELECT studio, COUNT(*) as total
FROM movies
GROUP BY studio
ORDER BY total DESC;

SELECT industry,
	   COUNT(*) as cnt,
       ROUND(AVG(imdb_rating),2) as avg_rating
FROM movies
GROUP BY industry;

SELECT studio,
	   COUNT(*) as cnt,
       ROUND(AVG(imdb_rating),2) as avg_rating
FROM movies
WHERE studio!="" -- skipping null data
GROUP BY studio
ORDER BY avg_rating DESC;