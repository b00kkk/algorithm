--solvesql multiplatform-games
WITH major AS (
  SELECT CASE WHEN p.name IN ('PS3', 'PS4', 'PSP', 'PSV') THEN 'SONY'
  WHEN p.name IN ('Wii', 'WiiU', 'DS', '3DS') THEN 'Nintendo'
  WHEN p.name IN ('X360', 'XONE') THEN 'Microsoft' END AS major_platform,
   g.name, g.platform_id, g.year
  FROM games g
  JOIN platforms p
  ON g.platform_id = p.platform_id
  WHERE year>=2012
)

SELECT m.name
FROM major m
JOIN platforms p
ON m.platform_id = p.platform_id
GROUP BY m.name
HAVING COUNT(DISTINCT major_platform)>=2