class Solution(object):
    def isPalindrome(self, x):
        inputX = x

        numReversed = 0

        while x > 0:
           
            originalNum = x

            rem = originalNum % 10    

            numReversed = numReversed * 10 + rem

            originalNum = x // 10
            
            x = originalNum

        return inputX == numReversed