import java.io.*;
import java.util.*;

class Main
{
    static int[][][] matrix;
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        matrix = new int[2][][];
        for(int t=0; t<2; t++){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            matrix[t] = new int[n][m];
            for(int i=0; i<n; i++){
                st = new StringTokenizer(br.readLine());
                for(int j=0; j<m; j++){
                    matrix[t][i][j] = Integer.parseInt(st.nextToken());
                }
            }
        }
        
        int[][] answer = new int[matrix[0].length][matrix[1][0].length];
        for(int i=0; i<matrix[0].length; i++){
            for(int j=0; j<matrix[0][0].length; j++){
                for(int k=0; k<matrix[1][0].length; k++){
                    answer[i][k] += matrix[0][i][j] * matrix[1][j][k];
                }
            }
        }
        
        for(int i=0; i<answer.length; i++){
            for(int j=0; j<answer[0].length; j++){
                System.out.print(answer[i][j]+" ");
            }
            System.out.println();
        }
    }
}