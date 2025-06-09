-- solvesql find-steadyseller-writers
WITH distinct_years AS (
  SELECT DISTINCT author, year
  FROM books
  WHERE genre = 'Fiction'),
minus_first_year AS (
  SELECT author, year, year - ROW_NUMBER() OVER(PARTITION BY author ORDER BY year) AS minus_year
  FROM distinct_years
  ORDER BY author, year
  ),
RESULT AS (
  SELECT author, minus_year, MAX(year) AS year, COUNT(*) AS depth
  FROM minus_first_year
  GROUP BY author, minus_year
  HAVING COUNT(*)>=5)

SELECT author, year, depth
FROM RESULT