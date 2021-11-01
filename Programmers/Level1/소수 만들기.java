class Solution {
    public static boolean is_prime(int number) {
 
		// 0 과 1 은 소수가 아니다
		if(number < 2) {
			return false;
		}
		
		// 2 는 소수다
		if(number == 2) {
			return true;
		}
		
        
		for(int i = 2; i < number; i++) {
			// 소수가 아닐경우
			if(number % i == 0) {
				return false;
			}
		}
		// 위 반복문에서 약수를 갖고 있지 않는경우 소수다.
		
		return true;
	}
    public int solution(int[] nums) {
        int answer = 0;
        
        for(int i = 0; i < nums.length -2 ; i ++){
            for(int j = i+1; j < nums.length - 1; j ++){
                for(int k = j + 1; k < nums.length; k ++){
                    if(is_prime(nums[i]+nums[j]+nums[k])){
                        answer += 1;
                    }
                }
            }
        }
        

        return answer;
    }
}
