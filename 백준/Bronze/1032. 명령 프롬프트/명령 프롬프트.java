import java.util.*;
import java.io.*;

class Main {
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		char[] s = br.readLine().toCharArray();
		
		for (int i = 0; i < N-1; i++) {
			char[] tmp = br.readLine().toCharArray();
			for (int j = 0; j < tmp.length; j++) {
				if (s[j] != tmp[j]) {
					String Q = "?";
					s[j] = Q.charAt(0);
				}
			}
		}
		System.out.println(s);
	}
}