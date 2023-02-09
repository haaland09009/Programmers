def solution(s):
    answer = ''
    s = s.lower() # 일단 문자열 전체를 모두 소문자로 변환시킨다.
    for i in s.split(' '): # 공백 기준으로 살펴보기
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j]
        answer += ' '        
                
    return answer[:-1]