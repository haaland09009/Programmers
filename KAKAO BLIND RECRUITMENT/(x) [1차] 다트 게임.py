def solution(dartResult):
    stack = []
    result = []
    dartResult = dartResult.replace('10', 'A')
    for i in dartResult:
        if i.isdigit() or i == 'A':
            stack.append(10 if i == 'A' else int(i))
        else:
            if i == 'S':
                result.append(stack.pop())
            elif i == 'D':
                result.append(stack.pop()**2)
            elif i == 'T':
                result.append(stack.pop()**3)
            elif i == '*' and len(result) >= 2:
                result[-1] = result[-1] * 2
                result[-2] = result[-2] * 2
            elif i == '*' and len(result) == 1:
                result[-1] = result[-1] * 2
            elif i == '#':
                result[-1] = result[-1] * (-1)   
    return sum(result)