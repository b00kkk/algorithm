--solvesql film-ending-with-consonant
SELECT title
FROM film
WHERE rating IN ('R','NC-17')
AND SUBSTR(title,-1,1) NOT IN ('A','E','I','O','U')