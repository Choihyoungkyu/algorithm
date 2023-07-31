import java.io.*;
import java.util.*;

class Main
{
    static int N;
    static List<Integer> in, post;
    static List<Integer> answer;
    static BufferedWriter bw;
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N = Integer.parseInt(br.readLine());
        List<String> tmp1 = Arrays.asList(br.readLine().split(" "));
        List<String> tmp2 = Arrays.asList(br.readLine().split(" "));
        in = new ArrayList<Integer>();
        post = new ArrayList<Integer>();
        for(int i=0; i<N; i++){
            in.add(Integer.parseInt(tmp1.get(i)));
            post.add(Integer.parseInt(tmp2.get(i)));
        }
        in_post_to_pre(in, post);
        bw.flush();
        bw.close();
    }

    private static void in_post_to_pre(List<Integer> in, List<Integer> post) throws IOException{
        if(post.size()>0){
            int root = post.get(post.size()-1);
            int mid = in.indexOf(root);
            bw.write(root+" ");
            in_post_to_pre(in.subList(0, mid), post.subList(0, mid));
            in_post_to_pre(in.subList(mid+1, in.size()), post.subList(mid, post.size()-1));
        }
    }

}