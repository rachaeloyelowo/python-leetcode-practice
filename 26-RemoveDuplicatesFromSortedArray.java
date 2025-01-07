class Solution {
    public int removeDuplicates(int[] nums) {
        int curr = nums[0];
        int index = 1;

        for (int i = 1; i < nums.length; i++){
            if (nums[i] != curr){
                curr = nums[i];
                nums[index] = curr;
                index++;
            }
        }
        return index;
    }
}