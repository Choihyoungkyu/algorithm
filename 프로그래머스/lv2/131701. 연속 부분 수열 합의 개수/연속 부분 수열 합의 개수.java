import java.util.HashSet;

class Solution {
    public int solution(int[] elements) {
        int[] newElements = new int[elements.length*2];
        for(int i=0; i<elements.length*2; i++){
            newElements[i] = elements[i%elements.length];
        }
        int answer = 0;
        HashSet<Integer> set = new HashSet<>();
        for(int i=1; i<elements.length+1; i++){
            int tmp;
            for(int j=0; j<elements.length; j++){
                tmp = 0;
                for(int k=1; k<=i; k++){
                    tmp += newElements[j+k];
                }
                set.add(tmp);
            }
        }
        return set.size();
    }
}