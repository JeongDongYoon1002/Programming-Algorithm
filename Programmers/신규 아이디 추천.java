class Solution {
    public String solution(String new_id) {
        String answer = "";
        // 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
        new_id = new_id.toLowerCase();
        
        // 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
        
		String temp = "";
		for(int i = 0; i < new_id.length(); i++) {
			char ch = new_id.charAt(i);

			if(ch >= 'a' && ch <= 'z') {
				temp += String.valueOf(ch);
			} else if(ch >= '0' && ch <= '9') {
				temp += String.valueOf(ch);
			} else if(ch == '.' || ch == '-' || ch == '_') {
				temp += String.valueOf(ch);
			}
		}
        // 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
        for(int i = 0; i < temp.length() - 1; i++){
            
            if(temp.charAt(i) == '.'){
                int j = i + 1;
                String dot = ".";
                while(j != temp.length() && temp.charAt(j) == '.'){
                    dot += ".";
                    j += 1;
                }
                if(dot.length() > 1){
                    temp = temp.replace(dot, ".");
                }
                    
            }
        }
        // 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
        if(temp.startsWith(".") ){
            temp = temp.substring(1, temp.length());
        }
        else if(temp.endsWith(".")){
            temp = temp.substring(0, temp.length()-1);
        }
        // 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
        if(temp.length() == 0){
            temp += "a";
        }
        // 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
        
        
        if(temp.length() >= 16){
            temp = temp.substring(0, 15);
        }
        // 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        if(temp.endsWith(".")){
            temp = temp.substring(0, temp.length()-1);
        }
        
        // 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
        String last = temp.charAt(temp.length()-1) + "";
        if(temp.length() == 2){
            temp = temp + last;
        }
        else if(temp.length() == 1){
            temp = temp + last + last;
        }

        System.out.println(temp);
        return temp;
    }
}
