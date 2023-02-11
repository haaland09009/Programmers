from collections import deque
def correct(x):
    stack = []
    result = True
    for i in x:
        if i == '[' or i == '(' or i == '{':
            stack.append(i)
        else:
            if stack == []:
                result = False
                break
            else:
                if i == ']':
                    if stack[-1] == '[':
                        stack.pop(-1)
                    else:
                        result = False
                        break
                elif i == ')':
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        result = False
                        break                        
                elif i == '}':
                    if stack[-1] == '{':
                        stack.pop(-1)   
                    else:
                        result = False
                        break
    if stack:
        result = False
    return result                        
                
def solution(s):
    answer = 0
    q = deque(s)
    cnt = 0
    tmp = []
    while cnt < len(s):
        q.rotate(-1)
        if correct(q):
            answer += 1
        cnt += 1   
    return answer








-------------------------------------------
from collections import deque
def correct(x):
    stack = []
    result = True
    for i in x:
        if i == '[' or i == '(' or i == '{':
            stack.append(i)
        else:
            if stack == []:
                result = False
                break
            else:
                if i == ']':
                    if stack[-1] == '[':
                        stack.pop(-1)
                    else:
                        result = False
                        break
                elif i == ')':
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        result = False
                        break                        
                elif i == '}':
                    if stack[-1] == '{':
                        stack.pop(-1)   
                    else:
                        result = False
                        break
    if stack:
        result = False
    return result    

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += correct(s[i:]+s[:i])
    return answer    
