--solvesql mentor-mentee-list
SELECT A.employee_id mentee_id, A.name mentee_name, B.employee_id mentor_id, B.name mentor_name
FROM
(SELECT *
FROM employees
WHERE join_date BETWEEN '2021-09-31' AND '2021-12-31') A
JOIN (SELECT *
FROM employees
WHERE join_date<='2019-12-31') B
ON A.department != B.department
ORDER BY mentee_id, mentor_id