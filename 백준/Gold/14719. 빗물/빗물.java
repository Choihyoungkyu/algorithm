import java.io.*;

class Main
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int H = Integer.parseInt(input[0]);
        int W = Integer.parseInt(input[1]);
        String[] tmp_blocks = br.readLine().split(" ");
        int[] blocks = new int[W];
        for(int i=0; i<W; i++){
            blocks[i] = Integer.parseInt(tmp_blocks[i]);
        }
        
        int maxV = blocks[0];
        int tmp_maxV = 0;
        int tmp = 0;
        int answer = 0;
        int i=0;
        while(i<W-1){
            i++;
            for(int j=i; j<W; j++){
                if(blocks[j] >= maxV){
                    answer += (j-i) * maxV - tmp;
                    i = j;
                    maxV = blocks[j];
                    tmp = 0;
                    tmp_maxV = 0;
                    break;
                } else if (blocks[j] > tmp_maxV){
                    tmp_maxV = blocks[j];
                    tmp += blocks[j];
                } else {
                    tmp += blocks[j];
                }
            }
            if(tmp != 0){
                for(int j=W-1; j>=i; j--){
                    if(blocks[j] == tmp_maxV){
                        answer += (j-i+1) * tmp_maxV - tmp;
                        i = j;
                        maxV = tmp_maxV;
                        tmp = 0;
                        tmp_maxV = 0;
                        break;
                    } else {
                        tmp -= blocks[j];
                    }
                }
            }
        }
        System.out.println(answer);
    }
}