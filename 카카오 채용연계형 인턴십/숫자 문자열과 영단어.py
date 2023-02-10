def solution(s):
    answer = ''
    dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
          'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    tmp = ''
    for i in s:
        tmp += i
        if tmp in dic.keys():
            answer += dic[tmp]
            tmp = ''
        elif tmp in dic.values():
            answer += tmp
            tmp = ''
            
    return int(answer)




def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
