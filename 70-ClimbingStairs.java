class Solution {
    public int climbStairs(int n) {
        int p1 = 1; //points to the second to last step
        int p2 = 1; //points to the last step
        for (int i = 0; i < n - 1; i++){
            int temp = p1; 
            p1 += p2; //for each step, p1 and p2 are added together and stored in p1
            p2 = temp; //for each step p2; shifts to become the former p1
        }
        return p1;
    }
}