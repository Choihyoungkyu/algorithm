
import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

class Main {
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] arr = br.readLine().split(" ");
		int N = Integer.parseInt(arr[0]);
		int K = Integer.parseInt(arr[1]);
		int L = Integer.parseInt(arr[2]);
//		System.out.println(N+" "+K+" "+L);
		
		if (K > L) {
			int tmp = L;
			L = K;
			K = tmp;
		}
//		System.out.println(K+" "+L);
		
		int cnt = 1;
//		System.out.println("\ncnt : "+cnt+"\nN : "+N+"\nK : "+K+"\nL : "+L);
		while (N > 1) {
			if (K%2 == 1 && L-K == 1) break;
			cnt += 1;
			K = (K+1)/2;
			L = (L+1)/2;
			N = N/2;
//			System.out.println("\ncnt : "+cnt+"\nN : "+N+"\nK : "+K+"\nL : "+L);
		}
		if (N==1 && L-K != 1) {
			System.out.println(-1);
		} else {
			System.out.println(cnt);
		}
		
	}
}