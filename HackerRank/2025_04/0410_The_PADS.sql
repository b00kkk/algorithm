--HackerRank The PADS
WITH RESULT AS (
    SELECT Name, Occupation, CONCAT(Name,"(",SUBSTR(Occupation,1,1),")") AS r
    FROM OCCUPATIONS
    ORDER BY r),
RESULT2 AS (
    SELECT CONCAT('There are a total of ',COUNT(*)," ",LOWER(Occupation),"s.") AS r
    FROM RESULT
    GROUP BY Occupation
    ORDER BY COUNT(*),Occupation)

SELECT r
FROM RESULT
UNION
SELECT r
FROM RESULT2
ORDER BY r