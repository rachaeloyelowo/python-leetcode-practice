class Solution(object):
    
    def twoSum(self, nums, target):
        def lengthTwo():
            if (nums[0] + nums[1] == target):
                return 0, 1
        
        def lengthThree():
            lengthTwo()
            if (nums[1] + nums[2] == target):
                return 1, 2
            elif (nums[0] + nums[2] == target):
                return 0, 2
        
        def lengthFour():
            lengthThree()
            if (nums[0] + nums[3] == target):
                return 0, 3
            elif (nums[1] + nums[3] == target):
                return 1, 3
            elif (nums[2] + nums[3] == target):
                return 2, 3

        if (len(nums) == 2):
            if (nums[0] + nums[1] == target):
                return 0, 1
        elif (len(nums) == 3):
            if (nums[0] + nums[1] == target):
                return 0, 1
            elif (nums[1] + nums[2] == target):
                return 1, 2
            elif (nums[0] + nums[2] == target):
                return 0, 2
        elif (len(nums) == 4):
            if (nums[0] + nums[1] == target):
                return 0, 1
            elif (nums[1] + nums[2] == target):
                return 1, 2
            elif (nums[0] + nums[2] == target):
                return 0, 2
            elif (nums[0] + nums[3] == target):
                return 0, 3
            elif (nums[1] + nums[3] == target):
                return 1, 3
            elif (nums[2] + nums[3] == target):
                return 2, 3
        else:
            return 0, 0