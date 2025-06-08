-- solvesql redefine-session
WITH prev_event_time AS (
  SELECT
    user_pseudo_id, event_timestamp_kst,
    LAG(event_timestamp_kst) OVER(ORDER BY event_timestamp_kst) AS prev_time
  FROM ga
  WHERE user_pseudo_id = 'S3WDQCqLpK'),
new_event AS (
  SELECT user_pseudo_id, event_timestamp_kst, prev_time,
    CASE WHEN DATETIME(TRIM(prev_time), '+1 hour') < event_timestamp_kst THEN 1
    WHEN prev_time IS NULL THEN 1
    ELSE 0 END AS session_event
  FROM prev_event_time),
session_num AS(
  SELECT
  user_pseudo_id, event_timestamp_kst,
  SUM(session_event) OVER(ORDER BY event_timestamp_kst ROWS UNBOUNDED PRECEDING) AS session_id
FROM new_event)

SELECT 
  user_pseudo_id, MIN(event_timestamp_kst) AS session_start, MAX(event_timestamp_kst) AS session_end
FROM session_num
GROUP BY user_pseudo_id, session_id
