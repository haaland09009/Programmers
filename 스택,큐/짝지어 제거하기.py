def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        # 문자열에서 같은 알파벳이 2개 붙어 있다면 제거
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop(-1)
            stack.pop(-1)
    if stack: # 스택에 남아있는 원소가 있다면 모두 짝지어 제거하기가 되지 않은 것.
        return 0
    else:
        return 1