--solvesql number-of-friends
WITH friend_a AS 
(SELECT user_id,COUNT(user_a_id) a_count
FROM edges
RIGHT OUTER JOIN users
ON edges.user_a_id = users.user_id
GROUP BY user_id),
friend_b AS 
(SELECT user_id, COUNT(user_b_id) b_count
FROM edges
RIGHT OUTER JOIN users
ON edges.user_b_id = users.user_id
GROUP BY user_id)

SELECT friend_a.user_id, 
CASE WHEN (a_count is not null AND b_count is not null) THEN a_count+b_count
WHEN a_count is not null THEN a_count
ELSE b_count END AS num_friends
FROM friend_a
JOIN friend_b
ON friend_a.user_id = friend_b.user_id
ORDER BY 2 DESC, 1