import java.io.*;
import java.util.*;

class Main
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] input = br.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int[] in = new int[N+1];
        List<LinkedList<Integer>> out = new ArrayList<LinkedList<Integer>>();
        
        for(int i=0; i<N+1; i++){
            in[i] = 0;
            out.add(new LinkedList<Integer>());
        }
        
        int a, b;
        
        for(int i=0; i<M; i++){
            input = br.readLine().split(" ");
            a = Integer.parseInt(input[0]);
            b = Integer.parseInt(input[1]);
            in[b]++;
            out.get(a).add(b);
        }

        Queue<Integer> que = new PriorityQueue<>();

        for(int i=1; i<N+1; i++){
            if(in[i] == 0){
                que.add(i);
            }
        }

        while(!que.isEmpty()){
            int idx = que.poll();
            bw.write(idx+" ");
            for(int i : out.get(idx)){
                in[i]--;
                if(in[i] == 0){
                    que.add(i);
                }
            }
        }
        bw.flush();
    }
}