// https://school.programmers.co.kr/learn/courses/30/lessons/68644

import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        
        Set<Integer> set = new HashSet<>();
        List<Integer> list = new ArrayList<>();
        
        for(int i=0; i<numbers.length; i++) {
            for(int j=0; j<numbers.length; j++) {
                if (i!=j) set.add(numbers[i] + numbers[j]);
            }
        }
        
        for(Integer s : set) {
            list.add(s);
        }
        
        answer = new int[list.size()];
        for(int i=0; i<list.size(); i++) {
            answer[i] = list.get(i);
        }
        Arrays.sort(answer);
        
        
        return answer;
    }
}
