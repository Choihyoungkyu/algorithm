import java.io.*;
import java.util.*;

class Main
{
    static int R, C, answer;
    static Character[][] board;
    static boolean[][] visited;
    static Stack<Character> stack = new Stack<>();
    static int[][] D = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    static Map<Character, Integer> check;
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new Character[R][C];
        visited = new boolean[R][C];
        check = new HashMap<>();
        for(int i=0; i<R; i++){
            String input = br.readLine();
            for(int j=0; j<C; j++){
                board[i][j] = input.charAt(j);
                check.putIfAbsent(input.charAt(j), 0);
            }
        }
        check.put(board[0][0], 1);
        DFS(0, 0, 1);
        System.out.println(answer);
    }

    private static void DFS(int ci, int cj, int cnt)
    {
        if(answer < cnt){
            answer = cnt;
        }
        if(!check.values().contains(0)) return;
        for(int[] dir : D){
            int ni=ci+dir[0], nj=cj+dir[1];
            if(0<=ni && ni<R && 0<=nj && nj<C && !visited[ni][nj] && check.get(board[ni][nj]) == 0 && !board[ci][cj].equals(board[ni][nj])){
                check.put(board[ni][nj], 1);
                visited[ni][nj] = true;
                DFS(ni, nj, cnt+1);
                if(!check.values().contains(0)) return;
                check.put(board[ni][nj], 0);
                visited[ni][nj] = false;
            }
        }
    }
}