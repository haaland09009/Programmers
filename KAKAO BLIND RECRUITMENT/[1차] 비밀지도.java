// https://school.programmers.co.kr/learn/courses/30/lessons/17681
import java.util.*;
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        String[] array1 = convertArr(arr1, n);
        String[] array2 = convertArr(arr2, n);
      
        for(int i=0; i<n; i++) {
            String str = "";
            for(int j=0; j<n; j++) {
                if (array1[i].charAt(j) == '1' || array2[i].charAt(j) == '1') {
                    str += "#";
                } else if (array1[i].charAt(j) == '0' && array2[i].charAt(j) == '0') {
                    str += " ";
                }
            }
            answer[i] = str;
        }
        
        return answer;
    }
    
    public String[] convertArr(int[] arr, int n) {
        
        String[] array = new String[n];
        
        for(int i=0; i<arr.length; i++) {
            String str = Integer.toBinaryString(arr[i]);
            String zero = "";
            if (str.length() < n) {
                for(int j=0; j<n-str.length(); j++) 
                    zero += "0";
            }
            str = zero + str;
            array[i] = str;
        }
        
        return array;
    }
}
