import java.io.*;
import java.util.Stack;

class Main
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String S1 = br.readLine();
        String S2 = br.readLine();
        int[][] LCS = new int[S2.length()+1][S1.length()+1];

        LCS[0][0] = 0;
        
        // LCS 배열 채우기
        for(int i=1; i<S2.length()+1; i++){
            for(int j=1; j<S1.length()+1; j++){
                if(S2.charAt(i-1) == S1.charAt(j-1)){
                    LCS[i][j] = LCS[i-1][j-1] + 1;
                } else {
                    LCS[i][j] = Math.max(LCS[i-1][j], LCS[i][j-1]);
                }
            }
        }

        int i=S2.length(), j=S1.length();
        Stack<Character> stack = new Stack<Character>();
        while(i>0 && j>0){
            if (LCS[i][j] == LCS[i-1][j]){
                i--;
            } else if (LCS[i][j] == LCS[i][j-1]) {
                j--;
            } else{
                stack.add(S2.charAt(i-1));
                i--;
                j--;
            } 
        }

        bw.write(LCS[S2.length()][S1.length()]+"\n");
        while(!stack.isEmpty()){
            bw.write(stack.pop());
        }
        bw.flush();
        bw.close();
    }
}