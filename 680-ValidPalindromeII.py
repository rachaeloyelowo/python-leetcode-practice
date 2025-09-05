class Solution:
    def validPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        reverse = ""
        while (lo < hi):
            if (s[lo] != s[hi]):

                reverse1 = s[lo + 1 : hi + 1][::-1]
                reverse2 = s[lo : hi][::-1]
                if (reverse1 == s[lo + 1 : hi + 1] or reverse2 == s[lo : hi]):
                    return True
                 
                return False
            lo += 1
            hi -= 1

        return True