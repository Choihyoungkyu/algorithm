// 
import java.io.*;
import java.util.*;

class Main
{
    static int T, F;
    static HashMap<String, String> Networks;
    static HashMap<String, Integer> NetworksLength;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws Exception
    {
        T = Integer.parseInt(br.readLine());
        for(int tc=0; tc<T; tc++){
            F = Integer.parseInt(br.readLine());
            Networks = new HashMap<>();
            NetworksLength = new HashMap<>();
            for(int f=0; f<F; f++){
                String[] input = br.readLine().split(" ");
                bw.append(union(input[0], input[1])+"\n");
            }
        }
        bw.flush();
        bw.close();
    }

    private static Integer union(String id1, String id2) {
        Networks.putIfAbsent(id1, id1);
        NetworksLength.putIfAbsent(id1, 1);
        Networks.putIfAbsent(id2, id2);
        NetworksLength.putIfAbsent(id2, 1);

        String[] tmp = {find(id1), find(id2)};
        Arrays.sort(tmp);
        
        if(tmp[0].equals(tmp[1])){
            return NetworksLength.get(tmp[0]);
        }

        Networks.put(tmp[1], tmp[0]);
        NetworksLength.put(tmp[0], NetworksLength.get(tmp[0]) + NetworksLength.get(tmp[1]));
        return NetworksLength.get(tmp[0]);
    }

    private static String find(String id)
    {
        if(Networks.get(id).equals(id)){
            return id;
        }
        return find(Networks.get(id));
    }
}
