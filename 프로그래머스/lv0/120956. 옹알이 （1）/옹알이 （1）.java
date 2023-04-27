import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        List<String> list = Arrays.asList(babbling);
        List<String> check = new ArrayList<String>(Arrays.asList("aya", "ye", "woo", "ma"));
        for (String bab: babbling) {
        	char[] st = bab.toCharArray();
            String str = "";
            for(int i=0; i<st.length; i++) {
                str += st[i];
                if (check.contains(str)) {
                    str = "";
                }
            }
            if (str.equals("")) {
                answer += 1;
            }
        }
        return answer;
    }
}