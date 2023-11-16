// https://school.programmers.co.kr/learn/courses/30/lessons/134240
import java.util.*;
class Solution {
    public String solution(int[] food) {
        String answer = "";
        
        String result1 = ""; String result2 = "";
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=1; i<food.length; i++) {
            map.put(i, food[i] / 2);
        }
        
        for (Integer key : map.keySet()) {
            int count = map.get(key);
            for(int i=0; i<count; i++) {
                result1 += key;
            }
        }
        
        for(int i=result1.length()-1; i>=0; i--) {
            result2 += result1.charAt(i);
        }
  
        answer = result1 + "0" + result2;
        
        return answer;
    }
}

