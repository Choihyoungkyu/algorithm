import java.io.*;
import java.util.*;

class Main
{
    static int N, ans1=0, ans2=0;
    static long maxV=Long.MAX_VALUE;
    static long[] nums;
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        nums = new long[N];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            nums[i] = Long.parseLong(st.nextToken());
        }
        solution();
        System.out.print(nums[ans1] < nums[ans2] ? nums[ans1]+" "+nums[ans2] : nums[ans2]+" "+nums[ans1]);
    }

    private static void solution()
    {
        for(int i=0; i<N; i++){
            binarySearch(i);
        }
    }

    private static void binarySearch(int idx)
    {
        int s=idx+1, e=N-1;
        while(s<=e){
            int m = (s+e)/2;
            long temp = Math.abs(nums[m] + nums[idx]);
            if(temp < maxV){
                maxV = temp;
                ans1 = idx;
                ans2 = m;
            }
            if(nums[m]+nums[idx] < 0){
                s = m+1;
            } else {
                e = m-1;
            }
        }
    }
}