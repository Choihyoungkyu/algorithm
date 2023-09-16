import java.util.*;

class Solution {
    static ArrayList<ArrayList<Integer>> adjL = new ArrayList<>();
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer;
        
        for(int[] road : roads) {
            int a=Math.min(road[0], road[1])-1, b=Math.max(road[0], road[1])-1;
            while(adjL.size() < b+1){
                adjL.add(new ArrayList<>());
            }
        
            adjL.get(a).add(b);
            adjL.get(b).add(a);
        }

        answer = dijkstra(n, sources, destination);
        return answer;
    }
    
    private static int[] dijkstra(int n, int[] sources, int destination) {
        int[] distances = new int[n];
        for(int i=0; i<n; i++){
            distances[i] = Integer.MAX_VALUE;
        }
        distances[destination-1] = 0;

        PriorityQueue<int[]> pque = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int[] start = {distances[destination-1], destination-1};
        pque.add(start);

        while(!pque.isEmpty()){
            int[] current = pque.poll();

            if(current[0] > distances[current[1]]) {
                continue;
            }

            for(int new_destination : adjL.get(current[1])) {
                int distance = current[0] + 1;
                if(distance < distances[new_destination]) {
                    distances[new_destination] = distance;
                    int[] next_destination = {distance, new_destination};
                    pque.add(next_destination);
                }
            }
        }

        int[] res = new int[sources.length];
        for(int i=0; i<sources.length; i++) {
            res[i] = distances[sources[i]-1] != Integer.MAX_VALUE ? distances[sources[i]-1] : -1;
        }
        return res;
    }
}