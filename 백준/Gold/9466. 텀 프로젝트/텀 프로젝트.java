import java.io.*;

class Main
{
    static int answer;
    static int[] arr;
    static boolean[] visited, done;
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for(int t=0; t<T; t++){
            int N = Integer.parseInt(br.readLine());
            String[] input = br.readLine().split(" ");
            arr = new int[N+1];
            visited = new boolean[N+1];
            done = new boolean[N+1];
            answer = N;

            for(int i=1; i<N+1; i++){
                arr[i] = Integer.parseInt(input[i-1]);
            }

            for(int i=1; i<N+1; i++){
                if(!done[i]){
                    DFS(i);
                }
            }
            
            bw.write(answer+"\n");
        }
        bw.flush();
        bw.close();
    }

    private static void DFS(int n){
        // 이미 방문 했을 때
        if(visited[n]){
            done[n] = true;
            answer--;
        } else {
            // 방문하지 않았을 때
            visited[n] = true;
        }

        // 다음 사람이 팀 결성을 아직 못했을 때
        if(!done[arr[n]]){
            DFS(arr[n]);
        }

        visited[n] = false;
        done[n] = true;
    }
}