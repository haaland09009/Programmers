def solution(phone_book):
    answer = True
    phone_book.sort()
    
    dic = {}
    
    for phone_number in phone_book:
        dic[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ''
        for number in phone_number:
            temp += number
            if temp in dic and temp != phone_number:
                answer = False
                break

    return answer


#------------------------
def solution(phone_book):
    answer = True
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            answer = False
            break
    return answer