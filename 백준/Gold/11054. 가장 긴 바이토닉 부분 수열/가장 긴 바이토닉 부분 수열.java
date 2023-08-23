// 골드4 / 
import java.io.*;
import java.util.*;

class Main
{
    static int N;
    static int[] nums;
    static int[] DP;
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        nums = new int[N];
        DP = new int[N];
        for(int i=0; i<input.length; i++){
            nums[i] = Integer.parseInt(input[i]);
            DP[i] = 0;
        }
        List<Integer> arr1 = LCS(true);
        List<Integer> arr2 = LCS(false);
        // System.out.println(arr1.toString());
        // System.out.println(arr2.toString());
        int maxV = 0;
        for(int i : DP){
            if(maxV < i){
                maxV = i;
            }
            // System.out.print(i+" ");
        }
        System.out.println(maxV-1);
    }
    
    private static List<Integer> LCS(boolean dir)
    {
        List<Integer> lcs = new ArrayList<>();
        lcs.add(0);
        if(dir){
            for(int i=0; i<N; i++){
                int lastNum = lcs.get(lcs.size()-1);
                if(lastNum < nums[i]){
                    lcs.add(nums[i]);
                } else {
                    int idx = binarySearch(lcs, nums[i]);
                    lcs.remove(idx);
                    lcs.add(idx, nums[i]);
                }
                DP[i] += lcs.size()-1;
            }
        } else {
            for(int i=N-1; i>=0; i--){
                int lastNum = lcs.get(lcs.size()-1);
                if(lastNum < nums[i]){
                    lcs.add(nums[i]);
                } else {
                    int idx = binarySearch(lcs, nums[i]);
                    lcs.remove(idx);
                    lcs.add(idx, nums[i]);
                }
                DP[i] += lcs.size()-1;
            }
        }
        return lcs;
    }

    private static int binarySearch(List<Integer> lcs, int num)
    {
        int s=0, e=lcs.size()-1;
        while(s<e){
            int m = (s+e)/2;
            if(lcs.get(m) < num){
                s = m+1;
            } else {
                e = m;
            }
        }
        return e;
    }
}
