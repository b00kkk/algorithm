-- solvesql flow-and-stock
SELECT strftime('%Y',acquisition_date) AS 'Acquisition year',
COUNT(*) AS 'New acquisitions this year (Flow)',
SUM(COUNT(*)) 
OVER(ORDER BY strftime('%Y',acquisition_date) ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
AS 'Total collection size (Stock)'
FROM artworks
WHERE acquisition_date IS NOT NULL
GROUP BY strftime('%Y',acquisition_date)
ORDER BY 'Acquistion year'