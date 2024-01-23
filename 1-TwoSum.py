class Solution(object):
    def twoSum(self, nums, target):

        hashMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[n] = i
        
        return