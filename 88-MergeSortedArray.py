class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        largest_list = m

        if (n > m):
            largest_list = n
        
        p2 = 0 # pointer for n
        for i in range(m, len(nums1)): # combines the arrays
            nums1[i] = nums2[p2]
            p2 += 1
        
        for i in range(len(nums1) - 1): # sorts the array
            min = nums1[i]
            for j in range(i + 1, len(nums1)):
                if (nums1[j] < min):
                    temp = nums1[i]
                    nums1[i] = nums1[j]
                    nums1[j] = temp
                    min = nums1[i]