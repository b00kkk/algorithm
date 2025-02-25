-- solvesql main-platform-of-game-developers
WITH games_sale AS(
  SELECT *, (sales_na+sales_eu+sales_jp+sales_other) AS sales_all
  FROM games
)
SELECT developer, platform, sales_sum AS sales
FROM
(SELECT c.name AS developer, p.name AS platform, SUM(sales_all) AS sales_sum,
 RANK() OVER (PARTITION BY c.name ORDER BY SUM(sales_all) DESC) AS rnk
FROM games_sale g JOIN platforms p
ON g.platform_id = p.platform_id
JOIN companies c
ON g.developer_id = c.company_id
GROUP BY c.name, p.name)
WHERE rnk=1