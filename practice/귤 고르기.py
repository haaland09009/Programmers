def solution(k, tangerine):
    tangerine.sort()
    
    dic = {}
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    count_list = [] # 귤의 종류를 담을 리스트
    answer = 0
    for a,b in sorted(dic.items(), key=lambda x:x[1], reverse=True):
        answer += b
        count_list.append(a) # 귤의 종류를 담는다.
        if answer >= k: # 지금까지 담은 귤의 수가 경화가 한 상자에 담으려는 귤의 수이거나 그 이상일 때
            return len(count_list)


# --------------------------------------------------------------------------------------------------------




from collections import Counter
def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine) # key와 그에 따른 value 딕셔너리 형태로 출력
    for v in sorted(count.values(), reverse = True):
        k -= v
        answer += 1 # 종류의 수 추가
        if k <= 0:
            break
 
    return answer

 