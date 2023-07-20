import java.util.*;
import java.io.*;

class Main
{
    static BufferedReader br;
    public static void main(String[] args) throws Exception
    {
        br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int i=0; i<T; i++){
            solution();
        }
        
    }
    
    static void solution() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        List<ArrayList<Integer>> indegree = new ArrayList<ArrayList<Integer>>();
        List<ArrayList<Integer>> outdegree = new ArrayList<ArrayList<Integer>>();

        for(int i=0; i<N+1; i++){
            indegree.add(new ArrayList<Integer>());
            outdegree.add(new ArrayList<Integer>());
        }

        int[] costs = new int[N+1];
        costs[0] = 0;
        
        st = new StringTokenizer(br.readLine());
        for(int i=1; i<N+1; i++){
            costs[i] = Integer.parseInt(st.nextToken());
        }
        
        for(int i=0; i<K; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            indegree.get(b).add(a);
            outdegree.get(a).add(b);
        }

        int target = Integer.parseInt(br.readLine());

        ArrayDeque<Integer> que = new ArrayDeque<Integer>();
        int[] DP = new int[N+1];
        Arrays.fill(DP, 0);

        for(int i=1; i<N+1; i++){
            if(indegree.get(i).isEmpty()){
                que.add(i);
                DP[i] = costs[i];
            }
        }

        while(!que.isEmpty()){
            int idx = que.poll();
            if(idx == target){
                System.out.println(DP[idx]);
                return;
            }
            for(int i : outdegree.get(idx)){
                DP[i] = Math.max(DP[idx] + costs[i], DP[i]);
                indegree.get(i).remove(indegree.get(i).indexOf(idx));
                if(indegree.get(i).isEmpty()) que.add(i);
            }
        }
    }
}
