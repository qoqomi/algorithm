import java.util.Arrays;

class Solution {
    public int solution(int[] mats, String[][] park) {
        Arrays.sort(mats);
        
        for(int i = mats.length - 1; i >= 0; i--) {
            int size = mats[i];
            
            for(int r = 0; r < park.length; r++) {
                for(int c = 0; c < park[0].length; c++) {
                    
                    boolean canPlace = true;
                    
                    for(int dr = 0; dr < size; dr++) {
                        for(int dc = 0; dc < size; dc++) {
                            int nr = r + dr;
                            int nc = c + dc;
                            
                            if(nr >= park.length || nc >= park[0].length) {
                                canPlace = false;
                            } else if(!park[nr][nc].equals("-1")) {
                                canPlace = false;
                            }
                        }
                    }
                    
                    if(canPlace) return size;
                }
            }
        }
        
        return -1;
    }
}