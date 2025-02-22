-- solvesql day-of-furniture
SELECT order_date, COUNT(DISTINCT CASE WHEN category='Furniture' THEN order_id END) AS furniture,
ROUND(COUNT(DISTINCT CASE WHEN category='Furniture' THEN order_id END)*100.0/COUNT(DISTINCT order_id),2) AS furniture_pct
FROM records
GROUP BY order_date
HAVING count(DISTINCT order_id)>=10
AND COUNT(DISTINCT CASE WHEN category='Furniture' THEN order_id END)*100.0/COUNT(DISTINCT order_id) >= 40
ORDER BY 3 DESC, 1