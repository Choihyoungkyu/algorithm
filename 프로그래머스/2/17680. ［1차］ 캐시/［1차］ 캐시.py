def solution(cacheSize, cities):
    answer = 0
    cashe = []
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        low_city = city.lower()
        if low_city not in cashe:
            if len(cashe) == cacheSize: 
                cashe.pop(0)
            cashe.append(low_city)
            answer += 5
        else: 
            cashe.remove(low_city)
            cashe.append(low_city)
            answer += 1
        # print(answer, cashe)
    return answer