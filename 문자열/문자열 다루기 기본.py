def solution(s):
    return True if (len(s) == 4 or len(s) == 6) and s.isdigit() else False
-----------------------------------------------------------------------------
str.isdigit() : 문자열이 숫자로만 이루어져 있는지 판단하는 것
음수를 뜻하는 '-', 소수점을 뜻하는 '.' 이것들을 숫자가 아닌 문자로 판단을 하기 때문에
실수나 음수를 판단하지 못한다.
즉, "-2".isdigit(), "1.234".isdigit() 둘다 False 가 나오게 된다.
정리하자면 "오직 0을 포함한 양수형 정수로만 이루어진 문자열"만 isdigit에서 True가 나올 수 있다.


