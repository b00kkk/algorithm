-- solvesql top-3-bill
SELECT day, time, sex, total_bill
FROM (SELECT *,RANK() OVER(PARTITION BY day ORDER BY total_bill DESC) AS rank
FROM tips)
WHERE rank<=3