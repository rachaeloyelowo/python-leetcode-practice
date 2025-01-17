class Solution {
    public int majorityElement(int[] nums) {
    
        int smallestVal = nums[0];
        for (int i = 0; i < nums.length - 1; i++){ //sort the array
            for (int j = i + 1; j < nums.length; j++){
                if (smallestVal > nums[j]){
                    int temp = smallestVal;
                    smallestVal = nums[j];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
        
        int overallCount = 0;
        int majority = nums[0];
        for (int i = 0; i < nums.length; i++){
            int val = nums[i];
            int count = 0;
            while (nums[i] == val){
                count++;
                if (i != nums.length - 1){
                    if (nums[i+1] == val){
                        i++;
                    } else {
                        break;
                    }
                } else {
                    break;
                }
            }
            if (count > overallCount){
                overallCount = count;
            }
        }
        
        return overallCount;
    }
}