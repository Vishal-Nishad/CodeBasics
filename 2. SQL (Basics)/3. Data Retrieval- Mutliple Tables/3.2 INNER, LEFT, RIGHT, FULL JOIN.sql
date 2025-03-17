SELECT * FROM movies;
SELECT * FROM financials;

-- getting error coz of ambiguous movie_id
SELECT movie_id, title, budget, revenue, currency, unit
FROM movies
JOIN financials
ON movies.movie_id=financials.movie_id;

-- correct one  ,,, by default it is performing inner join
SELECT m.movie_id, title, budget, revenue, currency, unit
FROM movies m
JOIN financials f
ON m.movie_id=f.movie_id;

-- left join
SELECT m.movie_id,title, budget, revenue, currency, unit
FROM movies m
LEFT JOIN financials f
ON m.movie_id=f.movie_id;

-- right join
SELECT f.movie_id,title, budget, revenue, currency, unit
FROM movies m
RIGHT JOIN financials f
ON m.movie_id=f.movie_id;

-- MY SQL does not support full join for achieving the result we have
-- to do union of left and right join
SELECT m.movie_id,title, budget, revenue, currency, unit
FROM movies m
LEFT JOIN financials f
ON m.movie_id=f.movie_id
UNION
SELECT f.movie_id,title, budget, revenue, currency, unit
FROM movies m
RIGHT JOIN financials f
ON m.movie_id=f.movie_id;

-- if both table has common column name , then we can use - USING keyword also
-- ex-
SELECT movie_id, title, budget, revenue, unit
FROM movies m
LEFT JOIN financials f
USING (movie_id);



-- EXERCISE QS
SELECT * FROM languages;
SELECT * From movies;

-- 1.qs
SELECT m.movie_id, m.title, m.industry, m.language_id, l.name
FROM movies m
LEFT JOIN languages l
ON m.language_id=l.language_id; 

-- 2.
SELECT m.movie_id, m.title, m.industry, m.language_id, l.name
FROM movies m
LEFT JOIN languages l
ON m.language_id=l.language_id 
WHERE name = "Telugu";

-- 3.
SELECT name, COUNT(name)
FROM movies m
LEFT JOIN languages l
ON m.language_id=l.language_id 
GROUP BY name;

SELECT 
            l.name, 
            COUNT(m.movie_id) as no_movies
	FROM languages l
	LEFT JOIN movies m USING (language_id)        
	GROUP BY language_id
	ORDER BY no_movies DESC;
