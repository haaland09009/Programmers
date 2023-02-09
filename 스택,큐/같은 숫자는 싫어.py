def solution(arr):
    stack = []
    for i in arr:
        stack.append(i)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop(-1)
    return stack