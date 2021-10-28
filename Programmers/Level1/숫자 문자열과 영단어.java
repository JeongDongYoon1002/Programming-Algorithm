class Solution {
    public int solution(String s) {
        String answer = "";
        String[] string_arr = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", 
"nine"};
        char[] int_arr = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
        String temp = "";
        
        for(int i = 0; i < s.length(); i ++){
            if( 'a' <= s.charAt(i) && s.charAt(i) <= 'z' ){
                temp += s.charAt(i);
                for(int j = 0; j < 10; j ++){
                    if(temp.equals(string_arr[j])){
                        answer += int_arr[j];
                        temp = "";
                        break;
                    }
                }
               
            }
            else{
                answer += s.charAt(i);
            }
        }
        return Integer.valueOf(answer);
    }
}
