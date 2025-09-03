class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmnPre = strs[0]

        # finds the shortest string and assumes it to be longest prefix

        shrtIndex = 0
        for i in range(len(strs)):
            if len(strs[i]) < len(cmnPre):
                cmnPre = strs[i]
                shrtIndex = i


        for i in range(len(strs)): # goes through each string
            if (i == shrtIndex): # skips shortest string
                continue

            s = strs[i] # s = each string in list

            for j in range(len(cmnPre)):
                if (cmnPre[j] != s[j]):
                    cmnPre = cmnPre[:j]
                    break

        return cmnPre