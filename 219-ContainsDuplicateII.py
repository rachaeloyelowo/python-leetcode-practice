class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates_dict = {} # creates a dictionary for the values in the list

        for i in range(len(nums)): # goes through the whole array
            if nums[i] in duplicates_dict: # checks if the current value is in the dictionary
                if abs(duplicates_dict[nums[i]] - i) <= k: # checks if the stored index of the value fulfils the condition
                    return True # if so, will return true, if not will update the index

            duplicates_dict[nums[i]] = i # adds the current value and index to dictionary if not there already
        return False