class Solution {
    public int climbStairs(int n) {

        if (n == 0){
            return 1;
        }

        int stairs = 0;
        if (n - 1 >= 0){
            stairs += climbStairs(n-1);
        }

        if (n - 2 >= 0){
            stairs += climbStairs(n-2);
        }

        return stairs;
    }
}