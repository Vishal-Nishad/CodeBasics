-- Retrieving all actors of movies with help of movie_actor and actors table
-- and then concatenating names in single row of individual movies
SELECT m.title , a.name
FROM movies m
JOIN movie_actor ma ON ma.movie_id=m.movie_id
JOIN actors a ON a.actor_id=ma.actor_id;

SELECT m.title, group_concat(a.name SEPARATOR " | ") as actors 
FROM movies m
JOIN movie_actor ma ON ma.movie_id=m.movie_id
JOIN actors a ON a.actor_id=ma.actor_id
GROUP BY m.movie_id;

SELECT a.name, group_concat(m.title SEPARATOR " | ") as movies,
COUNT(m.title) as movie_count
FROM actors a
JOIN movie_actor ma ON ma.actor_id=a.actor_id
JOIN movies m ON m.movie_id=ma.movie_id
GROUP BY a.actor_id
ORDER BY movie_count DESC;
