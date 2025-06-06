-- solvesql find-unnecessary-station-1
SELECT a.station_id, a.name
FROM station a
JOIN station b
ON a.station_id != b.station_id
AND
  2 * 6356 * ASIN(SQRT(
      POWER(SIN(RADIANS(a.lat - b.lat) / 2), 2) +
      COS(RADIANS(a.lat)) * COS(RADIANS(b.lat)) *
      POWER(SIN(RADIANS(a.lng - b.lng) / 2), 2)
    )) <= 0.3
AND
  a.updated_at < b.updated_at
GROUP BY a.station_id, a.name
HAVING COUNT(*)>=5