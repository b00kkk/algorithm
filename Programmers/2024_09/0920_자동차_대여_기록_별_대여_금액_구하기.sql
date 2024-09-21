/* Programmers 151141 */
SELECT DISTINCT(HISTORY_ID), 
CASE WHEN (DATEDIFF(END_DATE,START_DATE)+1)>=90 
THEN ROUND(DAILY_FEE*(DATEDIFF(END_DATE,START_DATE)+1)*(SELECT (100-DISCOUNT_RATE)*0.01 
                                            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                                            WHERE CAR_TYPE = '트럭' 
                                            AND DURATION_TYPE = '90일 이상'),0)
WHEN (DATEDIFF(END_DATE,START_DATE)+1)>=30
THEN ROUND(DAILY_FEE*(DATEDIFF(END_DATE,START_DATE)+1)*(SELECT (100-DISCOUNT_RATE)*0.01 
                                            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                                            WHERE CAR_TYPE = '트럭' 
                                            AND DURATION_TYPE = '30일 이상'),0)
WHEN (DATEDIFF(END_DATE,START_DATE)+1)>=7
THEN ROUND(DAILY_FEE*(DATEDIFF(END_DATE,START_DATE)+1)*(SELECT (100-DISCOUNT_RATE)*0.01 
                                            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                                            WHERE CAR_TYPE = '트럭' 
                                            AND DURATION_TYPE = '7일 이상'),0)                     ELSE ROUND(DAILY_FEE*(DATEDIFF(END_DATE,START_DATE)+1),0)
END FEE                    
FROM CAR_RENTAL_COMPANY_CAR C JOIN 
CAR_RENTAL_COMPANY_RENTAL_HISTORY H
ON C.CAR_ID = H.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
ON C.CAR_TYPE = P.CAR_TYPE
WHERE C.CAR_TYPE='트럭'
ORDER BY FEE DESC, HISTORY_ID DESC