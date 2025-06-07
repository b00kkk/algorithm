-- solvesql revenue-pct-per-category

WITH sum_sub_category AS (
  SELECT
    category, sub_category, SUM(sales) AS sales_sub_category
  FROM
    records
  GROUP BY category, sub_category),
sum_category AS (
  SELECT
    category, SUM(sales) AS sales_category
  FROM
    records
  GROUP BY category)

SELECT
  DISTINCT r.category, r.sub_category, ROUND(sales_sub_category,2) AS sales_sub_category,
  ROUND(sales_category,2) AS sales_category, ROUND(SUM(r.sales) OVER(),2) AS sales_total,
  ROUND((sales_sub_category/sales_category)*100,2) AS pct_in_category,
  ROUND((sales_sub_category/SUM(r.sales) OVER())*100,2) AS pct_in_total
FROM
  records AS r
JOIN sum_category AS c
ON r.category = c.category
JOIN sum_sub_category AS s
ON r.sub_category = s.sub_category AND r.category = s.category