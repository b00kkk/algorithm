--Hackerank Weather Observation Station 20
SELECT ROUND(LAT_N,4)
FROM (
    SELECT LAT_N,
           ROW_NUMBER() OVER (ORDER BY LAT_N) AS rn,
           COUNT(*) OVER () AS total_count
    FROM STATION
) AS sub
WHERE rn = FLOOR((total_count + 1)/2);
