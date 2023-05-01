import java.util.*;
import java.io.*;

public class Main {
	static int N;
	static int M;
	static int[][] arr;
	static int[][] visited;
	static int[][] DIR = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			if (N == 0 && M == 0) return;
			arr = new int[N][M];
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<M; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			visited = new int[N][M];
			for (int i=0; i<N; i++) {
				for (int j=0; j<M; j++) {
					visited[i][j] = 0;
				}
			}
			int cnt = 0;
			for (int i=0; i<N; i++) {
				for (int j=0; j<M; j++) {
					if (arr[i][j] == 1 && visited[i][j] == 0) {
						BFS(i, j);
						cnt += 1;
					}
				}
			}
			System.out.println(cnt);
		}
	}
	
	public static void BFS(int si, int sj) {
		Deque<int[]> queue = new ArrayDeque<int[]>();
		queue.offer(new int[] {si, sj});
		visited[si][sj] = 1;
		
		while(!queue.isEmpty()) {
			int[] cpos = queue.poll();
			int ci=cpos[0], cj=cpos[1];
			for(int[] D: DIR) {
				int ni=ci+D[0], nj=cj+D[1];
				if (0<=ni && ni<N && 0<=nj && nj<M && arr[ni][nj] == 1 && visited[ni][nj] == 0) {
					queue.offer(new int[] {ni, nj});
					visited[ni][nj] = 1;
				}
			}
		}
	}
}
