class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        
        // 남은 점들 체크
    	int[] arr = {0, 0, 0, 1};
        
        // 첫번째 점
        for (int i=0; i<3; i++) {
        	arr[i] = 1;
        	double slope1, slope2;

    		slope1 = getSlope(dots[i], dots[3]);
    		int tmp1=0, tmp2=0;
            
            // 남은 점들 체크
    		for (int k=0; k<3; k++) {
    			if (arr[k] == 0) {
                    // 3번째 점
    				if (tmp1 == 0) {
    					tmp1 = k;
                    // 4번째 점
    				} else {
    					tmp2 = k;
    					break;
    				}
    			}
    		}
            
    		slope2 = getSlope(dots[tmp1], dots[tmp2]);        		
            
    		if (slope1 == slope2) {
                // if (checkSame(slope1, dots[i], dots[tmp1])) {
        			return 1;                    
                // }
    		};
        	
            // 첫번째 점 초기화
			arr[i] = 0;
        }
        
        return 0;
    }
    
    public static double getSlope(int[] a1, int[] a2) {
    	double up = a1[1]-a2[1];
    	double down = a1[0]-a2[0];
    	return up/down;
    }
    
    public static boolean checkSame(double slope, int[] a1, int[] a2) {
        if ((double)(a2[1] - a1[1])/(double)(a2[0] - a1[0]) == slope){
            return false;
        };
        return true;
    }
}