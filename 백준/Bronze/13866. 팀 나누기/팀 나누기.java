
import java.util.*;
import java.io.*;

class Main {
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] arr = br.readLine().split(" ");
		int[] arr2 = new int[arr.length];
		for (int i = 0; i < arr.length; i++) {
			arr2[i] = Integer.valueOf(arr[i]);
		}
		System.out.println(Math.abs(arr2[0]+arr2[3]-(arr2[1]+arr2[2])));
	}
}