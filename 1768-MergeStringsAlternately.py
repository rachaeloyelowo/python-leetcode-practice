class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        n = len(word1)
        new_string = ""
        if (len(word1) > len(word2)):
            n = len(word2)

        for i in range(n):
            new_string = new_string + word1[p1]
            p1 += 1
            new_string = new_string + word2[p2]
            p2 += 1
        
        if (len(word1) > len(word2)):
            new_string = new_string + word1[p1:]
        elif (len(word1) < len(word2)):
            new_string = new_string + word2[p2:]
        
        return new_string