def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''
        for i in range(len(f)):
            if f[i].isdigit(): # 처음 숫자를 만나게 되면   
                head = f[:i] # 숫자를 만나기 이전까지 head
                number = f[i:] # 숫자를 만난 것부터 number
                
                for j in range(len(number)): # 처음 숫자를 만난 이후에  
                    if not number[j].isdigit(): # 숫자가 아닌 것을 만나게 되면
                        tail = number[j:]
                        number = number[:j]
                        break # 숫자 아닌 것을 만나면 바로 if문 종료
                answer.append((head,number,tail))
                break

    answer = sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))
 
    return [''.join(a) for a in answer]