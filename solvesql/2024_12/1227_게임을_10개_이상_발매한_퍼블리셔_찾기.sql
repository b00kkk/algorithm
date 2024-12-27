--solvesql publisher-with-many-games
SELECT c.name
FROM games g JOIN companies c
ON g.publisher_id = c.company_id
GROUP BY g.publisher_id
HAVING COUNT(g.game_id)>=10