import java.io.*;
import java.util.*;

class Main
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        
        int[] lst = new int[N];
        for(int i=0; i<N; i++){
            lst[i] = Integer.parseInt(st.nextToken());
        }

        int answer = Integer.MAX_VALUE;
        int tmp = lst[0];
        int i = 0;
        int j = 0;

        while(i<N && j<N){
            if(tmp >= S){
                answer = Math.min(answer, j-i+1);
            }
            if(i == j){
                if(i == N-1){
                    break;
                }
                j++;
                tmp += lst[j];
            } else if(j == N-1){
                tmp -= lst[i];
                i++;
            } else if(tmp < S){
                j++;
                tmp += lst[j];
            } else if (tmp >= S){
                tmp -= lst[i];
                i++;
            }
        }

        if(answer == Integer.MAX_VALUE){
            System.out.println(0);
        } else {
            System.out.println(answer);
        }
    }
}