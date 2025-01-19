--solvesql predict-game-scores-1
SELECT game_id, name, 
ROUND((CASE WHEN critic_score IS NULL THEN null_cs ELSE critic_score END),3) as critic_score,
CEIL((CASE WHEN critic_count IS NULL THEN null_cc ELSE critic_count END)) as critic_count,
ROUND((CASE WHEN user_score IS NULL THEN null_us ELSE user_score END),3) as user_score,
CEIL((CASE WHEN user_count IS NULL THEN null_uc ELSE user_count END)) as user_count
FROM games g
JOIN (SELECT genre_id, AVG(critic_score) null_cs, AVG(critic_count) null_cc,
AVG(user_score) null_us, AVG(user_count) null_uc
FROM games
GROUP BY genre_id) null_g
ON g.genre_id = null_g.genre_id
WHERE year >= 2015
AND (critic_score IS NULL
OR user_score IS NULL)