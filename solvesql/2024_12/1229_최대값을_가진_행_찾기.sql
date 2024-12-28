--solvesql max-row
SELECT id
FROM points
where x in
(SELECT max(x)
FROM points)
OR y in
(SELECT max(y)
FROM points)