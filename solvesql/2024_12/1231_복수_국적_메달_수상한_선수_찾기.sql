--solvesql multiple-medalist
SELECT name
FROM athletes a
JOIN records r
ON a.id = r.athlete_id
JOIN events e
ON r.event_id = e.id
JOIN games g
ON r.game_id = g.id
JOIN teams t
ON r.team_id = t.id
WHERE medal IS NOT NULL
AND year >= 2000
GROUP BY athlete_id
HAVING COUNT(DISTINCT t.team)>=2
ORDER BY name