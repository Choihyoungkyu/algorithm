import java.io.*;
import java.util.*;

class Main
{
    static int N;
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        Integer[][] arr = new Integer[N][];
        for(int i=0; i<N; i++){
            String[] stringArray = br.readLine().split(" ");
            Integer[] intArray = Arrays.stream(stringArray).map(Integer::parseInt).toArray(Integer[]::new);
            arr[i] = intArray;
        }

        Integer[][] DP = new Integer[N][];
        DP[0] = arr[0];

        for(int i=0; i<N-1; i++){
            DP[i+1] = new Integer[i+2];
            Arrays.fill(DP[i+1], 0);
            for(int j=0; j<i+1; j++){
                for(int k=j; k<j+2; k++){
                    DP[i+1][k] = Math.max(DP[i][j]+arr[i+1][k], DP[i+1][k]);
                }
            }
        }

        int maxV = 0;
        for(int i : DP[N-1]){
            if(i > maxV){
                maxV = i;
            }
        }
        System.out.println(maxV);
    }
}