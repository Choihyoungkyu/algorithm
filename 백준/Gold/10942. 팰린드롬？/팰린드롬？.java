import java.io.*;

class Main
{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String args[]) throws Exception
    {
        int N = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int[] nums = new int[N];
        for(int i=0; i<N; i++){
            nums[i] = Integer.parseInt(input[i]);
        }
        int M = Integer.parseInt(br.readLine());
        
        for(int i=0; i<M; i++){
            String[] tmp = br.readLine().split(" ");
            int S = Integer.parseInt(tmp[0]) - 1;
            int E = Integer.parseInt(tmp[1]) - 1;
            fn(S, E, nums);
        }
        bw.flush();
        bw.close();
    }

    static void fn(int S, int E, int[] nums) throws IOException{
        while(S<=E){
            if(nums[S] == nums[E]){
                S++;
                E--;
            } else {
                bw.write(0 + "\n");
                return;
            }
        }
        bw.write(1 + "\n");
        return;
    }
}