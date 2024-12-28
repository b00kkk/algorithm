--solvesql ratio-of-gifts
SELECT ROUND(100.0*g/t,3) ratio
FROM
(SELECT COUNT(*) g
FROM artworks
WHERE credit LIKE '%gift%') JOIN
(SELECT COUNT(*) t
FROM artworks)