
import java.util.*;
import java.io.*;

class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] DP = new int[N];
		if (N>6 | N==3 | N==5) {
			DP[0] = N-3;
		} else {
			DP[0] = N-1;
		}
		int idx = 0;
		if (DP[0]>0) {
			for (int i = 1; i < N; i++) {
				if (DP[i-1]>6 | DP[i-1]==3 | DP[i-1]==5) {
					DP[i] = DP[i-1]-3;
				} else {
					DP[i] = DP[i-1]-1;
				}
				if (DP[i]==0) {
					idx = i;
					break;
				}
			}
		}
		if (idx%2 == 0) {
			System.out.println("CY");
		} else {
			System.out.println("SK");
		}
	}
}