import java.io.*;
import java.util.*;


public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
		// 테스트케이스
		for (int tc=0; tc<T; tc++) {			
			// 입력 받기
			int N = Integer.parseInt(br.readLine());
			TreeSet<Integer> set = new TreeSet<Integer>();	// TreeSet 생성
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			for (int i=0; i<N; i++) {
				set.add(Integer.parseInt(st1.nextToken()));
			}
			
			int M = Integer.parseInt(br.readLine());
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			for (int i=0; i<M; i++) {
				int m = Integer.parseInt(st2.nextToken());
				boolean tmp = set.contains(m);
				if (tmp) {
					sb.append(1+"\n");					
				} else {					
					sb.append(0+"\n");
				}
				
			}
		}
        System.out.println(sb);
	}
}