-- solvesql redefine-session-2
WITH next_ga AS (
  SELECT
    user_pseudo_id, event_timestamp_kst, event_name, ga_session_id,
    LAG(event_timestamp_kst) OVER(ORDER BY event_timestamp_kst) AS next_time
  FROM ga
  WHERE user_pseudo_id = 'a8Xu9GO6TB'
  ORDER BY event_timestamp_kst),
result AS (
  SELECT user_pseudo_id, event_timestamp_kst, event_name, ga_session_id,
  CASE WHEN DATETIME(TRIM(next_time), '+10 minute')< event_timestamp_kst THEN 1
  WHEN next_time IS NULL THEN 1
  ELSE 0 END AS session_clear
  FROM next_ga)

SELECT 
  user_pseudo_id, event_timestamp_kst, event_name, ga_session_id,
  SUM(session_clear) OVER(ORDER BY event_timestamp_kst ROWS UNBOUNDED PRECEDING) AS new_session_id
FROM result