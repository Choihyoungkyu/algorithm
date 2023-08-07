import java.io.*;
import java.util.*;

class Main
{
    static int N, M;
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        Map<String, Integer> keywords = new HashMap<>();
        for(int i=0; i<N; i++){
            String tmp = br.readLine();
            if(!keywords.containsKey(tmp)){
                keywords.put(tmp, 1);
            } else {
                keywords.put(tmp, keywords.get(tmp)+1);
            }
        }
        for(int i=0; i<M; i++){
            String[] tmp_lst = br.readLine().split(",");
            for(String keyword : tmp_lst){
                if(keywords.containsKey(keyword)){
                    keywords.remove(keyword);
                }
            }
            System.out.println(keywords.keySet().size());
        }
    }
}