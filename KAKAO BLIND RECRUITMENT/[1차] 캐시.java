# https://school.programmers.co.kr/learn/courses/30/lessons/17680

import java.util.*;
class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        List<String> list = new ArrayList<>();
        
        for(String c : cities) {
            c = c.toLowerCase();
            if (list.contains(c)) {
                list.remove(c);
                list.add(c);
                answer += 1;
            } else if (!list.contains(c)) {
                list.add(c);
                answer += 5;
                if (list.size() == cacheSize + 1) {
                    list.remove(0);
                }
            }
        }
        
        return answer;
    }
}
