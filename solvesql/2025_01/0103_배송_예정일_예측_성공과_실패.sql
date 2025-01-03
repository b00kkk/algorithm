--solvesql estimated-delivery-date
SELECT STRFTIME('%Y-%m-%d',order_purchase_timestamp) purchase_date,
COUNT(CASE WHEN order_estimated_delivery_date>=order_delivered_customer_date THEN 1 END) success,
COUNT(CASE WHEN order_estimated_delivery_date<order_delivered_customer_date THEN 1 END) fail
FROM olist_orders_dataset
WHERE STRFTIME('%Y-%m',order_purchase_timestamp)='2017-01'
GROUP BY purchase_date
ORDER BY 1