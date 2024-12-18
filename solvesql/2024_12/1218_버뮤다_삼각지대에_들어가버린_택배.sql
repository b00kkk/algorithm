--solvesql shipment-in-bermuda
SELECT STRFTIME('%Y-%m-%d',order_delivered_carrier_date) delivered_carrier_date, COUNT(*) orders
FROM olist_orders_dataset
WHERE order_delivered_carrier_date IS NOT NULL
AND order_delivered_customer_date IS NULL
AND order_delivered_carrier_date BETWEEN '2017-01-01' AND '2017-02-01'
GROUP BY delivered_carrier_date
ORDER BY 1