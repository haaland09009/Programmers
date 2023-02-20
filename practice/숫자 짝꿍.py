from collections import Counter
def solution(X, Y):
    answer = ''
    inner = Counter(X) & Counter(Y)
    if len(list(inner)) == 0:
        return '-1'
    else:
        for k,v in sorted(inner.items(), key=lambda x:int(x[0]), reverse=True):
            answer += str(k) * v
            if answer[0] == '0':
                return '0'
    return answer

#------------------------------------------
def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer