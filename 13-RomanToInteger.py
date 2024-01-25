class Solution(object):
   def romanToInt(self, s):
       
        sepRoman = list(s)

        newInt = 0

        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        y = len(sepRoman)


        for x in range(y):
            if sepRoman[0] in romanDict:
                if sepRoman[0] == "I":
                    
                    if sepRoman[1] == "V" or "X":
                        romanDict.get(sepRoman[0]) - 1
                    else:
                        pass
                    
                elif sepRoman[0] == "X":


                    if sepRoman[1] == "L" or "C":
                        romanDict.get(sepRoman[0]) - 10
                    else:
                        pass
                elif sepRoman[0] == "C":


                    if sepRoman[1] == "D" or "M":
                        romanDict.get(sepRoman[0]) - 100
                    else:
                        pass
                else:
                    newInt = newInt + romanDict.get(sepRoman[0])

                del sepRoman[0]

        return newInt
