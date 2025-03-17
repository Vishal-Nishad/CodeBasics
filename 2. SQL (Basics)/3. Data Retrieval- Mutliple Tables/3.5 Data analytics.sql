USE moviesdb;
SELECT * FROM movies;
SELECT * FROM financials;

SELECT m.movie_id, title, release_year, budget, revenue, unit,
	(revenue-budget) as profit
FROM movies m
JOIN financials f
ON m.movie_id = f.movie_id;

SELECT m.movie_id, title, release_year, budget, revenue, unit,
	(revenue-budget) as profit
FROM movies m
JOIN financials f
ON m.movie_id = f.movie_id
WHERE industry="Bollywood"
ORDER BY profit DESC;

SELECT m.movie_id, title, release_year, budget, revenue, unit,
	CASE
		WHEN unit="Thousands" THEN ROUND((revenue-budget)/1000,1)
        WHEN unit="Billions"  THEN ROUND((revenue-budget)*1000,1)
        ELSE ROUND((revenue-budget),1)
	END as profit_millions
FROM movies m
JOIN financials f
ON m.movie_id = f.movie_id
WHERE industry="Bollywood"
ORDER BY profit_millions DESC;