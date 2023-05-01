-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT(ONLINE_SALE.USER_ID)) AS USERS
FROM (
    SELECT USER_ID, GENDER FROM USER_INFO
) AS USER_LIST
RIGHT JOIN ONLINE_SALE ON USER_LIST.USER_ID = ONLINE_SALE.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER
ORDER BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER
# SELECT * FROM ONLINE_SALE