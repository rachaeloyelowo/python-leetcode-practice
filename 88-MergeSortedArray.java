class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (m == 0){
            for (int i = 0; i < nums1.length; i++){
                nums1[i] = nums2[i]; 
            }
        } else if (n != 0 && m != 0){
            int nPointer = 0;
            for (int i = m; i < nums1.length; i++){
                nums1[i] = nums2[nPointer];
                nPointer++;
            }
            for (int i = 0; i < nums1.length; i++){
                for (int j = i + 1; j < nums1.length; j++){
                    if (nums1[j] < nums1[i]){
                        int temp = nums1[i];
                        nums1[i] = nums1[j];
                        nums1[j] = temp;
                    }
                }
            }
        }
    }
}