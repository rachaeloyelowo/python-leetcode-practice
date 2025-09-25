class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {

        }

        for x in nums : 
            if x not in dictionary :
                dictionary[x] = True
            else :
                dictionary[x] = False

        for d in dictionary :
            if dictionary[d] : 
                return d
        
        return
