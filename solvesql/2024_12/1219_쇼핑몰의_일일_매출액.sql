--solvesql olist-daily-revenue
SELECT strftime('%Y-%m-%d',order_purchase_timestamp) dt, ROUND(SUM(payment_value),3) revenue_daily
FROM olist_orders_dataset d
JOIN olist_order_payments_dataset p
ON d.order_id=p.order_id
WHERE dt >= '2018-01-01'
GROUP BY dt