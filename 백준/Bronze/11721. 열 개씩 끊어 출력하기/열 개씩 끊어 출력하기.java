import java.util.*;
import java.io.*;
class Main {
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
//		int n = sc.nextInt();
		String s = sc.next();
		String msg = "";
//		char[] arr = new char[s.length()];
		for (int i = 0; i < s.length(); i++) {
			msg += s.charAt(i);
			if (msg.length() == 10) {
				System.out.println(msg);
				msg = "";
			}
		}
		if (msg != null) {
			System.out.println(msg);
		}	
	}
}