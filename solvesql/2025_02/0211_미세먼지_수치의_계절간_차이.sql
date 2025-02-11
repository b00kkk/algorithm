--solvesql finedust-seasonal-summary
SELECT 
CASE WHEN strftime('%m-%d',measured_at) BETWEEN '03-01' AND '05-31' THEN 'spring'
WHEN strftime('%m-%d',measured_at) BETWEEN '06-01' AND '08-31' THEN 'summer'
WHEN strftime('%m-%d',measured_at) BETWEEN '09-01' AND '11-31' THEN 'autumn'
ELSE 'winter' END season,
MEDIAN(pm10) pm10_median, ROUND(AVG(pm10),2) pm10_average
FROM measurements
GROUP BY season