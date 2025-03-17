-- having clause
SELECT release_year, COUNT(release_year) as cnt
FROM movies
WHERE imdb_rating>6
GROUP BY release_year
HAVING cnt>2
ORDER BY cnt DESC;



SELECT * FROM actors;
-- Pinting current age from birth_year column
SELECT *, YEAR(CURDATE())-birth_year as age
FROM actors;

SELECT * FROM financials;
SELECT *,(revenue-budget) as profit 
FROM financials;

-- Using IF Function
-- Syntax for IF: IF(condition,true,false)
SELECT *, 
IF (currency="USD", revenue*84,revenue) as revenue_inr
FROM financials;


SELECT distinct unit FROM financials;

-- CASE END

SELECT *,
CASE
	WHEN unit="Thousands" THEN revenue/1000
    WHEN unit="Billions"  THEN revenue*1000
    ELSE revenue -- same as WHEN unit="Millions" THEN revenue
END as revenue_million
FROM financials;


-- 2.12 Exercise question
SELECT *,(revenue-budget) as profit,
	((revenue-budget)*100)/budget as profit_percentage
FROM financials;