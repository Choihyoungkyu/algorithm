import java.io.*;
import java.util.*;

class Main
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<int[]> lines = new ArrayList<>();
        for(int i=0; i<N; i++){
            String[] tmp = br.readLine().split(" ");
            int[] lst = {Integer.parseInt(tmp[0]), Integer.parseInt(tmp[1])};
            lines.add(lst);
        }
        Collections.sort(lines, (e1, e2) -> e1[0] - e2[0]);
        
        List<Integer> LIS = new ArrayList<>();
        LIS.add(0);
        for(int i=0; i<lines.size(); i++){
            int n = lines.get(i)[1];
            if(LIS.get(LIS.size()-1) < n){
                LIS.add(n);
            } else {
                int left=0, right=LIS.size();
                while(left<right){
                    int mid = (left+right)/2;
                    if(LIS.get(mid) < n){
                        left = mid + 1;
                    } else{
                        right = mid;
                    }
                }
                LIS.remove(right);
                LIS.add(right, n);
            }
        }
        System.out.println(lines.size()-LIS.size()+1);
    }
}