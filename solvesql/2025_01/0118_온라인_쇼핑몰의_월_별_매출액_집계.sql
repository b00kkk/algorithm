--solvesql shoppingmall-monthly-summary
SELECT a.order_month, ordered_amount, canceled_amount, (ordered_amount + canceled_amount) total_amount
FROM (SELECT strftime('%Y-%m',order_date) order_month, SUM(price*quantity) ordered_amount
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
WHERE o.order_id NOT LIKE 'C%'
GROUP BY order_month) a
JOIN
(SELECT strftime('%Y-%m',order_date) order_month, SUM(price*quantity) canceled_amount
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
WHERE o.order_id LIKE 'C%'
GROUP BY order_month) b
ON a.order_month = b.order_month
ORDER BY 1