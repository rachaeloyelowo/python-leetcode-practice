class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        odd_mid = True
        mid = floor(len(s) / 2) # finds the middle value
        if (len(s) % 2 == 0): # checks if there is an actual middle
            odd_mid = False
                
        temp = 0
        for i in range(mid):
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp