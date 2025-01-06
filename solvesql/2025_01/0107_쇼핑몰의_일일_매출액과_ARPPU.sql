--solvesql daily-arppu
SELECT STRFTIME('%Y-%m-%d',order_purchase_timestamp) dt, count(DISTINCT customer_id) pu,
SUM(payment_value) revenue_daily, ROUND(SUM(payment_value)/count(DISTINCT customer_id),2) arppu
FROM olist_orders_dataset a
JOIN olist_order_payments_dataset b
ON a.order_id=b.order_id
WHERE dt>='2018-01-01'
GROUP BY dt