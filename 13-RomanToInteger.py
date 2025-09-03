class Solution:
    def romanToInt(self, s: str) -> int:
        romanNums = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        num = 0
        nxtIndex = 1
        skipNxt = False
        

        for char in s:
            if skipNxt:
                skipNxt = False
                nxtIndex += 1
                continue
            

            if nxtIndex < len(s) and romanNums[s[nxtIndex]] > romanNums[char]:
                skipNxt = True
                num -= romanNums[char]
                num += romanNums[s[nxtIndex]]
            else:
                num += romanNums[char]

            nxtIndex += 1
            
            

        return num