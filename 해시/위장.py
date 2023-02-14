def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = [cloth[0]]
        else:
            dic[cloth[1]].append(cloth[0])
    
    for k,v in dic.items():
        answer *= (len(v)+1)
        
    return answer - 1 # 아무것도 안 입는 경우를 제외해야하기 때문에 1을 뺀다.







def solution(clothes):
    clothes_type = {}

    for n,t in clothes: # name, type
        if t not in clothes_type:
            clothes_type[t] = 2 # 입는 경우와 안 입는 경우가 있으므로 2
        else:
            clothes_type[t] += 1

    answer = 1
    for value in clothes_type.values():
        answer *= value

    return answer - 1 