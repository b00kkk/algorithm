/* Programmers 157339 */
SELECT *
FROM 
(
    SELECT CC.CAR_ID, CC.CAR_TYPE, ROUND(DAILY_FEE*30*(100-DISCOUNT_RATE)*0.01) as FEE
    FROM CAR_RENTAL_COMPANY_CAR CC
        LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY CH ON CC.CAR_ID = CH.CAR_ID
                                                        AND CH.START_DATE <= '20221130' 
                                                        AND CH.END_DATE >= '20221101'
        LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN CP ON CC.CAR_TYPE = CP.CAR_TYPE
                                                        AND CP.DURATION_TYPE = '30일 이상' 
    WHERE CC.CAR_TYPE IN ('SUV', '세단')
      AND CH.CAR_ID IS NULL
) A
WHERE A.FEE >= 500000 AND A.FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC