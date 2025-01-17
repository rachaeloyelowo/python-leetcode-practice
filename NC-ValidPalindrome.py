class Solution:
    def isPalindrome(self, s: str) -> bool:
        eligible_characters = "abcdefghijklmnopqrstuvwxyz0123456789" # all characters to be compared
        
        lo = 0 # lower pointer
        hi = len(s) - 1 # higher pointer
        
        while (lo < hi):
            if (str(s[lo].lower()) not in eligible_characters):
                lo += 1
                continue
            if (str(s[hi].lower()) not in eligible_characters):
                hi -= 1
                continue
            if (str(s[lo].lower()) != str(s[hi].lower())):
                return False
            else:
                lo += 1
                hi -= 1

        return True