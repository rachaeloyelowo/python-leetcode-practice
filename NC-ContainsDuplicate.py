class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {} #creates a dictionary

        for i in range(len(nums)): #goes through nums array
            if (duplicates.get(nums[i]) == True): #checks if the array value is in dict
                return True
            else:
                duplicates[nums[i]] = True #adds the array value if not in dict
        return False