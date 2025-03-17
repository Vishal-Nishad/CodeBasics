SELECT * FROM movies;
SELECT * FROM financials;
SELECT * FROM languages;

SELECT m.title, revenue, unit,
CASE 
	WHEN unit="Billions" THEN revenue*1000
	WHEN unit="Thousands" THEN revenue/1000
    ELSE revenue
END as revenue_mln
FROM languages l
JOIN movies m ON l.language_id=m.language_id
JOIN financials f ON f.movie_id=m.movie_id
WHERE l.name="Hindi"
ORDER BY revenue_mln DESC;

SELECT m.title, revenue, unit,
CASE 
	WHEN unit="Billions" THEN revenue*1000
	WHEN unit="Thousands" THEN revenue/1000
    ELSE revenue
END as revenue_mln
FROM movies m
JOIN financials f ON m.movie_id=f.movie_id
JOIN languages l ON m.language_id=l.language_id
WHERE l.name="Hindi"
ORDER BY revenue_mln DESC;