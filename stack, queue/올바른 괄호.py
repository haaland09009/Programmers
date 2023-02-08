def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else: # ')'일 경우
            if len(stack) == 0: # 스택이 비어있다면
                answer = False
                break
            else: # 스택에 원소가 있을 경우
                stack.pop(-1)
    if stack: # 스택에 원소가 남아있다면
        answer = False
    return answer