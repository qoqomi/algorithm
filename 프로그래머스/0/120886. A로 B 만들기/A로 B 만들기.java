import java.util.Arrays;
class Solution {
    public int solution(String before, String after) {
        int answer = 0;
        char[] a = after.toCharArray();
        char[] b = before.toCharArray();
        
        Arrays.sort(a);
        Arrays.sort(b);
        
        System.out.println(a);
        System.out.println(b);
        
        if(Arrays.equals(a,b)){
            answer = 1;
        }
            
        
        return answer;
    }
}