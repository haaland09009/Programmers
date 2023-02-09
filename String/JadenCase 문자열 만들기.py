def solution(s):
    answer = ''
    s = s.lower()
    for i in s.split(' '):
        for j in range(len(i)):
            if j == 0:
                answer += i[j].upper()
            else:
                answer += i[j]
        answer += ' '        
                
    return answer[:-1]