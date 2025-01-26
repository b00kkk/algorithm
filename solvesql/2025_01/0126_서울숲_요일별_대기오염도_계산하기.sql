--solvesql weekday-stats-airpollution
SELECT 
    CASE 
        WHEN strftime('%w', measured_at) = '0' THEN '일요일'
        WHEN strftime('%w', measured_at) = '1' THEN '월요일'
        WHEN strftime('%w', measured_at) = '2' THEN '화요일'
        WHEN strftime('%w', measured_at) = '3' THEN '수요일'
        WHEN strftime('%w', measured_at) = '4' THEN '목요일'
        WHEN strftime('%w', measured_at) = '5' THEN '금요일'
        WHEN strftime('%w', measured_at) = '6' THEN '토요일'
    END weekday,
    ROUND(AVG(no2), 4) no2,
    ROUND(AVG(o3), 4) o3,
    ROUND(AVG(co), 4) co,
    ROUND(AVG(so2), 4) so2,
    ROUND(AVG(pm10), 4) pm10,
    ROUND(AVG(pm2_5), 4) pm2_5
FROM measurements
GROUP BY weekday
ORDER BY 
  CASE 
    WHEN weekday = '월요일' THEN 0
    WHEN weekday = '화요일' THEN 1
    WHEN weekday = '수요일' THEN 2
    WHEN weekday = '목요일' THEN 3
    WHEN weekday = '금요일' THEN 4
    WHEN weekday = '토요일' THEN 5
    WHEN weekday = '일요일' THEN 6 END