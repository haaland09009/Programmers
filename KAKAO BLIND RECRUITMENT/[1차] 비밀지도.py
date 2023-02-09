def solution(n, arr1, arr2):
    temp_1, temp_2 = [], []
    
    for arr in arr1:
        ls = [] # arr1의 원소 하나 당 이진변환 결과를 담을 리스트
        tmp = bin(arr)[2:] # 이진변환한 결과
        if len(tmp) < n: # 만약 자릿수가 주어진 n보다 모자를 경우, 앞 자리에 모자란 자릿수만큼 0 채워주기
            tmp = '0'*(n-len(tmp)) + tmp
        for t in tmp:
            ls.append(t)
        temp_1.append(ls)    
            
    for arr in arr2:
        ls = [] 
        tmp = bin(arr)[2:]
        if len(tmp) < n:
            tmp = '0'*(n-len(tmp)) + tmp
        for t in tmp:
            ls.append(t)
        temp_2.append(ls)              
    
    answer = []
    for i in range(len(temp_1)):
        sum_ls = '' # 두 개의 결과를 합친 것
        for j in range(len(temp_1[i])):
            if temp_1[i][j] == '0' and temp_2[i][j] == '0':
                sum_ls += ' '
            elif temp_1[i][j] == '1' or temp_2[i][j] == '1':
                sum_ls += '#'       
        answer.append(sum_ls)
            
    return answer