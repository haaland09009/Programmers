# https://school.programmers.co.kr/learn/courses/30/lessons/70129

import java.util.*;
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int count = 0;
        
        while (!s.equals("1")) {
            for (int i=0; i<s.length(); i++) {
                if (s.charAt(i) == '0') {
                    count++;
                }
            }
            answer[1] += count;
            s = Integer.toBinaryString(s.length() - count);
            count = 0;
            answer[0]++;
        }
        
        return answer;
        
    }
}
