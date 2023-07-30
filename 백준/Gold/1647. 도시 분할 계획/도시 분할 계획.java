import java.io.*;
import java.util.*;

class Main
{
    static int N, M;
    static Path[] paths;
    static int[] p;
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        p = new int[N+1];
        paths = new Path[M];
        for(int i=0; i<N+1; i++){
            p[i] = i;
        }
        for(int i=0; i<M; i++){
            input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            int c = Integer.parseInt(input[2]);
            paths[i] = new Path(a, b, c);
        }
        List<Path> pathList = Arrays.asList(paths);
        pathList.sort(null);

        int answer = 0;
        int maxV = 0;
        for(int i=0; i<M; i++){
            int x, y;
            x = pathList.get(i).a;
            y = pathList.get(i).b;
            if(find(x) != find(y)){
                union(x, y);
                int c = pathList.get(i).c;
                answer += c;
                maxV = c;
            }
        }
        answer -= maxV;
        System.out.println(answer);
    }

    private static void union(int a, int b){
        a = find(a);
        b = find(b);
        if(a > b){
            p[a] = b;
        } else {
            p[b] = a;
        }
    }

    private static int find(int x){
        if(p[x] == x){
            return x;
        } else {
            return find(p[x]);
        }
    }

    private static class Path implements Comparable<Path>
    {
        int a, b, c;

        public Path(int a, int b, int c){
            this.a = a;
            this.b = b;
            this.c = c;
        }

        @Override
        public int compareTo(Path other){
            return Integer.compare(c, other.c);
        }
    }
}