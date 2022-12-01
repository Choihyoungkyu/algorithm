
import java.util.*;
import java.io.*;

class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {			
			String[] arr = br.readLine().split(" ");
			int N = Integer.parseInt(arr[0]);
			int M = Integer.parseInt(arr[1]);
			int cnt = 0;
			String[] arr1 = br.readLine().split(" ");
			ArrayList<Integer> nums = new ArrayList<>();
			for (String num : arr1) {
				nums.add(Integer.parseInt(num));
			}
			for (int j = 0; j < N; j++) {
				cnt += 1;
				int maxV = 0;
				int idx = 0;
				for (int k = 0; k < N; k++) {
					if (maxV < nums.get(k)) {
						maxV = nums.get(k);
						idx = k;
					}
				}
				if (idx==M) {
					System.out.println(cnt);
					break;
				}
//				System.out.println(nums);
				nums.remove(idx);
				nums.add(idx, 0);
//				System.out.println(idx);
//				System.out.println("처음 : " + nums);
				for (int k = 0; k < idx; k++) {
					nums.add(nums.get(k));
					M -= 1;
				}
//				System.out.println("중간 : " + nums);
				for (int k = 0; k < idx; k++) {
					nums.remove(0);
				}
//				System.out.println("끝 : " + nums);
//				System.out.println("");
				if (M<0) {
					M += N;
				}
			}
		}
	}
}