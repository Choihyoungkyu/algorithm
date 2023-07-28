import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i : tangerine){
            if(map.containsKey(i)){
                map.put(i, map.get(i)+1);
            } else {
                map.put(i, 1);
            }
        }
        Object[] cnts = map.values().toArray();
        Arrays.sort(cnts);
        int sum = 0;
        for(int i=cnts.length-1; i>=0; i--){
            answer++;
            sum += (int) cnts[i];
            if(k <= sum){
                break;
            }
        }
        return answer;
    }
}