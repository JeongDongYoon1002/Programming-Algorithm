import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int i = 0;
        
        List<Integer> list = new ArrayList<Integer>();
        while (answer < nums.length/2){
            if(i == nums.length) break;
          
          
            if(!list.contains(nums[i])){
                list.add(nums[i]);
                answer += 1;
            }
            
            i ++; 
            
        } 
        return answer;
    }
}
