
import java.util.*;
import java.io.*;

class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String[] arr = br.readLine().split(" ");
		int budget = Integer.parseInt(br.readLine());
		int[] nums = new int[N];
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(arr[i]);
		}
		Arrays.sort(nums);
		int maxV = 0;
		for (int i = 0; i < N; i++) {
			int avg = budget / (N-i);
			if (nums[i] <= avg) {
				budget -= nums[i];
				maxV = nums[i];
			} else {
				budget -= avg;				
				maxV = avg;
				break;
			}
		}
		System.out.println(maxV);
	}
}