-- 코드를 입력하세요
SELECT AI.NAME, AI.DATETIME
FROM ANIMAL_INS AI
LEFT OUTER JOIN ANIMAL_OUTS AO
USING (ANIMAL_ID)
WHERE AO.ANIMAL_ID is null
ORDER BY AI.DATETIME
LIMIT 3