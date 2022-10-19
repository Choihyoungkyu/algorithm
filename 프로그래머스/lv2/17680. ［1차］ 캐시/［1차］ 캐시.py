def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in range(len(cities)):
        # cache hit
        if cities[i].lower() in cache:
            cache.pop(cache.index(cities[i].lower()))
            cache.append(cities[i].lower())
            answer += 1
        # cache miss
        else:
            if len(cache) == cacheSize and cache:
                cache.pop(0)
                cache.append(cities[i].lower())
            else:
                if cacheSize == 0:
                    pass
                else:
                    cache.append(cities[i].lower())     
            answer += 5
            
    return answer