-- 코드를 작성해주세요
SELECT 
    A.ID
    , CASE WHEN A.RANKING <= B.TOTAL / 4 THEN 'CRITICAL'
           WHEN A.RANKING <= B.TOTAL / 2 THEN 'HIGH'
           WHEN A.RANKING <= B.TOTAL * 0.75 THEN 'MEDIUM'
           ELSE 'LOW'
      END AS COLONY_NAME
FROM 
    (
    SELECT A.ID
         , RANK() OVER (ORDER BY A.SIZE_OF_COLONY DESC) AS RANKING
         , 1 AS GO
     FROM ECOLI_DATA A
    ) A
    LEFT OUTER JOIN (
       SELECT 
            COUNT(*) AS TOTAL
          , 1 AS GO
       FROM ECOLI_DATA
    ) B 
    ON A.GO = B.GO
ORDER BY A.ID
