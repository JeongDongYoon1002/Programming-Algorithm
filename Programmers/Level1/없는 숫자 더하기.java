class Solution {
    public int solution(int[] numbers) {
        int answer = -1;
        int[] arr = {0,0,0,0,0,0,0,0,0,0};
        for(int num: numbers){
            arr[num] = 1;
        }
        for(int i = 0; i < 10; i ++){
            if(arr[i] == 0){
                answer += i;
            }
        }
     
        return answer+1;
    }
}
