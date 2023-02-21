def solution(elements):
    answer = 0
    elements_2 = elements * 2
    result = set()
    
    i = 1
    while i <= len(elements):
        for j in range(len(elements)):
            result.add(sum(elements_2[j:j+i]))
        i += 1    
    return len(result)