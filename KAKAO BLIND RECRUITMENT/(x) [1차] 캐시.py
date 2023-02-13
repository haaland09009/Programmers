def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        elif city not in cache:
            cache.append(city)
            answer += 5
            if len(cache) == cacheSize + 1:
                cache.pop(0)
    return answer