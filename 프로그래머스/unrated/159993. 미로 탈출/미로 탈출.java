import java.util.ArrayDeque;

class Solution {
    static int N;
    static int M;
    public int solution(String[] maps) {
        int answer = 0;
        N = maps.length;
        M = maps[0].length();
        int[][] visited1 = new int[N][M];
        int[][] visited2 = new int[N][M];
        Current s=null, e=null, v=null;
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                visited1[i][j] = Integer.MAX_VALUE;
                visited2[i][j] = Integer.MAX_VALUE;
                if(maps[i].charAt(j) == 'S'){
                    s = new Current(i, j);
                } else if(maps[i].charAt(j) == 'E'){
                    e = new Current(i, j);
                } else if(maps[i].charAt(j) == 'L'){
                    v = new Current(i, j);
                }
            }
        }
        int StoV = BFS(visited1, maps, s, v);
        int VtoE = BFS(visited2, maps, v, e);
        answer = StoV>0 && VtoE>0 ? StoV+VtoE : -1;
        return answer;
    }
    
    static int BFS(int[][] visited, String[] maps, Current s, Current e){
        visited[s.i][s.j] = 0;
        ArrayDeque<Current> deque = new ArrayDeque<>();
        deque.add(new Current(s.i, s.j));
        Current[] D = {new Current(0, 1), new Current(0, -1), new Current(1, 0), new Current(-1, 0)};
        while(!deque.isEmpty()){
            Current c = deque.poll();
            for(Current d : D){
                Current n = new Current(c.i+d.i, c.j+d.j);
                if(0<=n.i && n.i<N && 0<=n.j && n.j<M && maps[n.i].charAt(n.j)!='X' && visited[n.i][n.j] == Integer.MAX_VALUE){
                    visited[n.i][n.j] = visited[c.i][c.j]+1;
                    if(n.i == e.i && n.j == e.j) return visited[n.i][n.j];
                    deque.add(new Current(n.i, n.j));
                }
            }
        }
        return 0;
    }
    
    static class Current{
        int i, j;
        
        Current(int i, int j){
            this.i = i;
            this.j = j;
        }
    }
}