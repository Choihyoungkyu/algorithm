import java.io.*;
import java.util.*;

class Main
{
    static int N, K;
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        K = Integer.parseInt(input[1]);

        PriorityQueue<int[]> que = new PriorityQueue<>(Comparator.comparingInt(a -> -a[1]));
        int[][] jewels = new int[N][2];
        for(int i=0; i<N; i++){
            input = br.readLine().split(" ");
            int[] tmp = {Integer.parseInt(input[0]), Integer.parseInt(input[1])};
            jewels[i] = tmp;
        }

        int[] bags = new int[K];
        for(int i=0; i<K; i++){
            bags[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(jewels, (e1, e2) -> e1[0] - e2[0]);
        Arrays.sort(bags);

        long answer = 0;
        int idx = 0;

        for(int c : bags){
            while(idx<N){
                if(jewels[idx][0] <= c){
                    que.offer(jewels[idx++]);
                } else break;
            }
            if(!que.isEmpty()){ 
                answer += que.poll()[1];
            }
        }
        System.out.println(answer);
    }
}