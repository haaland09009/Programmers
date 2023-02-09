def solution(s):
    return True if (len(s) == 4 or len(s) == 6) and s.isdigit() else False

--------------------------
#### 참고
 str.isdigit() : 문자열이 숫자로만 이루어져 있는지 판단하는 것
음수를 뜻하는 '-', 소수점을 뜻하는 '.' 이것들은 숫자가 아닌 문자로 판단을 하므로
실수나 음수를 판단하지 못합니다.
즉, "-2".isdigit(), "1.234".isdigit() 둘다 False
"오직 0을 포함한 양수형 정수로만 이루어진 문자열"만 isdigit에서 True가 나올 수 있다.

출처: https://blockdmask.tistory.com/556
--------------------------
