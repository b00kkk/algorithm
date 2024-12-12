--solvesql join
SELECT DISTINCT athlete_id
FROM events e JOIN records r
ON e.id=r.event_id
WHERE e.sport='Golf'