import java.io.*;

class Main
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] d = new int[N+1];
        for(int i=0; i<N; i++){
            String[] nums = br.readLine().split(" ");
            for(int j=0; j<2; j++){
                d[i+j] = Integer.parseInt(nums[j]);
            }
        }

        int[][] DP = new int[N+1][N+1];
        for(int l=0; l<N; l++){
            for(int i=1; i<N-l; i++){
                int j = i + l + 1;
                DP[i][j] = Integer.MAX_VALUE;
                for(int k=i; k<j; k++){
                    DP[i][j] = Math.min(DP[i][j], DP[i][k]+DP[k+1][j]+(d[i-1]*d[k]*d[j]));
                }
            }
        }

        System.out.println(DP[1][N]);
    }
}
