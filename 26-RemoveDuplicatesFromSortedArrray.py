class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        current_num = nums[0]
        new_nums = []

        i = 0
        while (i < len(nums)):
            new_nums.append(nums[i])
            k += 1
            if (i != len(nums) - 1): # makes sure not at end of array
                
                current_num = nums[i]

                while (current_num == nums[i+1]):
                    i += 1
                    if (i == len(nums) - 1):
                        break
            i += 1

        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        
        return k
