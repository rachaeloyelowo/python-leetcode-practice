class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != val){
                k++;
            }
        }
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == val){
                for (int j = i; j < nums.length; j++){
                    if (nums[j] != val){
                        nums[i] = nums[j];
                        nums[j] = val;
                        break;
                    }
                }
            }
        }
        return k;
    }
}