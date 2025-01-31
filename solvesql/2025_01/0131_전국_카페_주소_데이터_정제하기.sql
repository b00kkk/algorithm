--solvesql refine-cafe-address
SELECT SUBSTR(address,1,INSTR(address," ")-1) sido,
TRIM(SUBSTR(LTRIM(SUBSTR(address,INSTR(address," ")+1)),1,INSTR(SUBSTR(address,INSTR(address," ")+1)," "))) sigungu,
COUNT(*) cnt
FROM cafes
GROUP BY sido, sigungu
ORDER BY cnt DESC