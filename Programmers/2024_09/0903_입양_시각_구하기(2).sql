/* Programmers 59413 */
SET @HOUR := -1; /*변수선언*/

SELECT (@HOUR := @HOUR+1) AS HOUR,
(SELECT COUNT(*)
 FROM ANIMAL_OUTS
WHERE HOUR(DATETIME)=@HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR<23

/* @HOUR 변수에 -1을 넣어줌 ( := 기호는 대입 )
WHERE 절에서 23미만일때까지 대입되어 0~23까지 생성됨 */