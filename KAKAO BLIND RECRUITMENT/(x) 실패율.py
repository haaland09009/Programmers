def solution(N, stages): 
    dic = {x:0 for x in range(1, N+1)}
    sum_list = [0] * (N+2)
    
    stages.sort()
    people = len(stages)
    
    for i in stages:
        sum_list[i] += 1
    
    for i in range(1, N+1):
        if people != 0:
            dic[i] = sum_list[i] / people
            people -= sum_list[i]
        
    return sorted(dic, key=lambda x:dic[x], reverse=True)