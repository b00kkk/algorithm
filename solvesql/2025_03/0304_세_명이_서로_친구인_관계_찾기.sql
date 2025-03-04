-- solvesql friend-group-of-3
SELECT a.user_a_id, a.user_b_id, b.user_b_id AS user_c_id
FROM edges a
JOIN edges b
ON a.user_b_id = b.user_a_id
JOIN edges c
ON (a.user_a_id = c.user_a_id
AND b.user_b_id = c.user_b_id)
WHERE (a.user_a_id<a.user_b_id
AND a.user_b_id<b.user_b_id)
AND 3820 IN (a.user_a_id, a.user_b_id, b.user_b_id)