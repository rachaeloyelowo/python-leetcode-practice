class Solution {
    public int mySqrt(int x) {
        int low = 1;
        int hi = x;
        int res = 0;
        
        while (low <= hi){
            int mid = low + ((hi - low) / 2);
            if (mid <= x / mid){
                low = mid + 1;
                res = mid;
            } else {
                hi = mid - 1;
            }
        }
        return res;
    }
}