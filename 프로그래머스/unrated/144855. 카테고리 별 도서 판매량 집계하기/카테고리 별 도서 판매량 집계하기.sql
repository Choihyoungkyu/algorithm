-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK
JOIN BOOK_SALES USING(BOOK_ID)
WHERE TO_CHAR(SALES_DATE, 'YYYY-MM-DD') >= '2022-01-01' AND TO_CHAR(SALES_DATE, 'YYYY-MM-DD') < '2022-02-01'
GROUP BY CATEGORY

ORDER BY CATEGORY
;