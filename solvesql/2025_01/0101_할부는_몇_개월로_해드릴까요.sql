--solvesql installment-month
SELECT payment_installments, COUNT(DISTINCT order_id) order_count, 
MIN(payment_value) min_value, MAX(payment_value) max_value, AVG(payment_value) avg_value
FROM olist_order_payments_dataset
WHERE payment_type='credit_card'
GROUP BY payment_installments