import java.io.*;
import java.util.*;

class Main
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for(int i=0; i<N; i++){
            String[] command = br.readLine().split(" ");
            if(command[0].equals("push")){
                queue.add(Integer.parseInt(command[1]));
            } else if(command[0].equals("pop")){
                if(queue.isEmpty()){
                    System.out.println(-1);
                } else {
                    System.out.println(queue.pop());
                }
            } else if(command[0].equals("size")){
                System.out.println(queue.size());
            } else if(command[0].equals("empty")){
                if(queue.isEmpty()){
                    System.out.println(1);
                } else{
                    System.out.println(0);
                }
            } else if(command[0].equals("front")){
                if(queue.isEmpty()){
                    System.out.println(-1);
                } else{
                    System.out.println(queue.getFirst());
                }
            } else if(command[0].equals("back")){
                if(queue.isEmpty()){
                    System.out.println(-1);
                } else{
                    System.out.println(queue.getLast());
                }
            }
        }
    }
}