--solvesql characteristics-of-orders
SELECT DISTINCT region Region,
COUNT(DISTINCT CASE WHEN category='Furniture' THEN order_id END) Furniture,
COUNT(DISTINCT CASE WHEN category='Office Supplies' THEN order_id END) 'Office Supplies',
COUNT(DISTINCT CASE WHEN category='Technology' THEN order_id END) Technology
FROM records
WHERE country='United States'
GROUP BY region