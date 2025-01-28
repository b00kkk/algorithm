--solvesql find-unnecessary-station-2
WITH rent AS (
  SELECT rent_station_id,
  SUM(CASE WHEN STRFTIME('%Y-%m',rent_at)='2018-10' THEN 1 ELSE 0 END) rent_18,
  SUM(CASE WHEN STRFTIME('%Y-%m',rent_at)='2019-10' THEN 1 ELSE 0 END) rent_19
  FROM rental_history
  GROUP BY rent_station_id
),
return AS (
  SELECT return_station_id,
  SUM(CASE WHEN STRFTIME('%Y-%m',return_at)='2018-10' THEN 1 ELSE 0 END) return_18,
  SUM(CASE WHEN STRFTIME('%Y-%m',return_at)='2019-10' THEN 1 ELSE 0 END) return_19
  FROM rental_history
  GROUP BY return_station_id
),
by_per AS (
  SELECT rent_station_id station_id, ROUND((rent_19+return_19)*100.0/(rent_18+return_18),2) usage_pct
  FROM rent 
  JOIN return
  ON rent.rent_station_id = return.return_station_id
  WHERE (rent_19+return_19)<>0
  AND (rent_18+return_19)<>0
)

SELECT a.station_id, name, local, usage_pct
FROM by_per a
JOIN station b
ON  a.station_id = b.station_id
WHERE usage_pct<=50