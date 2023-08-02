-- 코드를 입력하세요
SELECT DISTINCT CAR_ID
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = '세단'
    AND CAR_ID IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE EXTRACT(month FROM START_DATE) = 10
    )
ORDER BY CAR_ID DESC;