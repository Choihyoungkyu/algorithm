-- 코드를 입력하세요
SELECT 
    HISTORY_ID, 
    CAR_ID, 
    TO_CHAR(start_date, 'YYYY-MM-DD') as START_DATE, 
    TO_CHAR(end_date, 'YYYY-MM-DD') as END_DATE, 
    case 
        when (END_DATE - START_DATE) >= 29 then '장기 대여'
        else '단기 대여'
    end
    as RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE extract(month from start_date) = 9 and extract(year from start_date) = 2022
ORDER BY HISTORY_ID desc