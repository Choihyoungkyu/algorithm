-- 코드를 입력하세요
SELECT a.FOOD_TYPE, a.REST_ID, a.REST_NAME, a.FAVORITES
FROM REST_INFO a, (
    SELECT FOOD_TYPE, MAX(FAVORITES) as max_favorites
    FROM REST_INFO
    GROUP BY FOOD_TYPE
) b
WHERE a.FOOD_TYPE = b.FOOD_TYPE
GROUP BY a.FOOD_TYPE, a.REST_ID, a.REST_NAME, a.FAVORITES, b.max_favorites
HAVING a.FAVORITES = b.max_favorites
ORDER BY FOOD_TYPE DESC
;