--solvesql daily-revenue
SELECT day, sum(total_bill) revenue_daily
FROM tips
GROUP BY day
HAVING revenue_daily>=1000
ORDER BY revenue_daily DESC