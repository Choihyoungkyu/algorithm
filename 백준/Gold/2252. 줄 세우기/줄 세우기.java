import java.util.*;
import java.io.*;

class Main
{
    static int N, M;
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        ArrayDeque<Integer> que = new ArrayDeque<Integer>();
        List<ArrayList<Integer>> adjL_in = new ArrayList<ArrayList<Integer>>();
        List<ArrayList<Integer>> adjL_out = new ArrayList<ArrayList<Integer>>();

        for(int i=0; i<N+1; i++) {
            adjL_in.add(new ArrayList<Integer>());
            adjL_out.add(new ArrayList<Integer>());
        }

        for(int i=0; i<M; i++){
            input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            adjL_in.get(b).add(a);
            adjL_out.get(a).add(b);
        }

        for(int i=1; i<N+1; i++){
            if(adjL_in.get(i).size() == 0){
                que.add(i);
            }
        }

        while (!que.isEmpty()) {

            int idx = que.removeFirst();
            answer.append(idx).append(' ');

            for(int i : adjL_out.get(idx)) {
                adjL_in.get(i).remove(adjL_in.get(i).indexOf(idx));
            }

            for(int i : adjL_out.get(idx)) {
                if (adjL_in.get(i).size() == 0) {
                    que.add(i);
                }
            }
        }
        
        System.out.println(answer);
    }
}