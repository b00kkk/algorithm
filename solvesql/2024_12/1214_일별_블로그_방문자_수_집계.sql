-- solvesql blog-counter
SELECT strftime('%Y-%m-%d',event_date_kst) dt, COUNT(DISTINCT user_pseudo_id) users
FROM ga
WHERE event_date_kst BETWEEN '2021-08-02' AND '2021-08-09'
GROUP BY dt
ORDER BY dt