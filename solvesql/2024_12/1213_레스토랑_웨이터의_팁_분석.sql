--solvesql tip-analysis
SELECT day, time, ROUND(avg(tip),2) avg_tip, ROUND(avg(size),2) avg_size
FROM tips
GROUP BY day, time
ORDER BY day, time