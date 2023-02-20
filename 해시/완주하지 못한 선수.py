def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]    # completion 리스트에서 반복문을 도는 동안 조건에 만족하는 것이 없다면 참가자 리스트 중에서 가장 마지막에 있는 원소가 출력
        
#-----------------------------------------
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]   # = list(answer)[0]

#-----------------------------------------
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
