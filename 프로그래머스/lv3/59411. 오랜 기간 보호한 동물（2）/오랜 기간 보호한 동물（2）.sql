-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME 
FROM(
    SELECT ANIMAL_ID, NAME, outs.DATETIME - ins.DATETIME AS PERIOD
    FROM ANIMAL_INS ins
    JOIN ANIMAL_OUTS outs USING (ANIMAL_ID, NAME)
    ORDER BY PERIOD DESC
)
WHERE rownum <= 2