SELECT SUM(c1.population)
FROM city AS c1
    JOIN country AS c2
        ON c1.countrycode = c2.code
WHERE c2.continent = 'asia'