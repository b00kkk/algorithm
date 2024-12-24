--solvesql bad-finedust-measure
WITH next_measurements AS(
SELECT measured_at today, LEAD(measured_at) OVER(ORDER BY measured_at) next_day,
pm10, lead(pm10) OVER(ORDER BY measured_at) next_pm10
FROM measurements)
SELECT today, next_day, pm10, next_pm10
FROM next_measurements
WHERE pm10<next_pm10