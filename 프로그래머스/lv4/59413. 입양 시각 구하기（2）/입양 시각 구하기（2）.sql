-- 코드를 입력하세요
-- 몇 시에 입양이 가장 활발하게 일어나는지(0시 ~ 23시) 모든 시간 데이터를 생성
WITH RECURSIVE TIME AS(
    SELECT 0 as hour            # 초기값 설정
    UNION ALL                   # 위 쿼리와 아래 쿼리의 값을 연산
    SELECT hour + 1 FROM time   # 하나씩 불려 나감
    WHERE HOUR < 23)            # 반복을 멈추는 용도
    
SELECT TIME.HOUR, COUNT(ANIMAL_TYPE) AS COUNT FROM (
    SELECT *, HOUR(DATETIME) AS hour FROM ANIMAL_OUTS) AS OUTS
RIGHT JOIN TIME ON OUTS.HOUR = TIME.HOUR
GROUP BY TIME.HOUR
ORDER BY TIME.HOUR;

# WITH RECURSIVE TIME AS(
#     SELECT 0 as hour
#     UNION ALL
#     SELECT hour + 1 FROM time
#     WHERE HOUR < 23)

# SELECT TIME.HOUR, COUNT(animal_id) FROM (
#     SELECT *, HOUR(datetime) AS hour FROM animal_outs) AS outs2
#     RIGHT JOIN time ON outs2.hour = time.hour
# GROUP BY time.hour
# ORDER BY time.hour