import java.io.*;
import java.util.*;

class Main
{
    static int N;
    static boolean[] nums;
    static ArrayList<Integer> primes;

    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        if(N == 1){
            System.out.println(0);
            return;
        }
        nums = new boolean[N+1];
        for(int i=2; i<N+1; i++){
            nums[i] = true;
        }
        solution();
    }

    static void getPrimes(){
        for(int i=2; i<N+1; i++){
            if(nums[i]){
                for(int j=2*i; j<N+1; j+=i){
                    nums[j] = false;
                }
            }
        }
        primes = new ArrayList<Integer>();
        for(int i=2; i<N+1; i++){
            if(nums[i]){
                primes.add(i);
            }
        }
    }

    static void solution(){
        getPrimes();
        int i=0;
        int j=0;
        int sum=primes.get(0);
        int answer=0;

        while(i<primes.size()){
            if(sum<N){
                if(j<primes.size()-1){
                    j++;
                    sum += primes.get(j);
                } else {
                    sum -= primes.get(i);
                    i++;
                }
            } else if(sum==N){
                answer++;
                sum -= primes.get(i);
                i++;
            } else if(sum>N){
                sum -= primes.get(i);
                i++;
            }
        }
        System.out.println(answer);
    }
}