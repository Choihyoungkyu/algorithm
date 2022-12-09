
import java.util.*;
import java.io.*;

class Main {
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		ArrayList<Integer> arr = new ArrayList<>(N);
		HashMap<Integer, Integer> map = new HashMap<>();
		int tot = 0;
		int cnt = 0;
		ArrayList<Integer> maxV = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			if (map.containsKey(num)) {
				map.put(num, map.get(num)+1);
				if (cnt < map.get(num)) {
					cnt = map.get(num);
					maxV.clear();
					maxV.add(num);
				} else if (cnt == map.get(num)) {
					maxV.add(num);
				}
			} else {
				map.put(num, 1);
			}
//			System.out.println("최빈값 : "+maxV);
			arr.add(num);
			tot += num;
		}
//		System.out.println(map);
//		System.out.println(arr);
		Collections.sort(arr);
		
		double first = tot/(N*1.00);
		
		System.out.println((int) Math.floor(first+0.5));
		System.out.println(arr.get(N/2));
		if (maxV.size() >= 2) {
			Collections.sort(maxV);
			System.out.println(maxV.get(1));
		} else {
			if (maxV.size() == 1) {
				System.out.println(maxV.get(0));
			} else {
				if (arr.size() >= 2) {				
					System.out.println(arr.get(1));
				} else {
					System.out.println(arr.get(0));
				}	
			}
		}
		System.out.println(arr.get(N-1)-arr.get(0));
	}
}