class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphanumeric( char ) : 
            if (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122): # checking for alphanumerical values
                return True
            
            return False

        s = s.lower()

        stack = []

        for char in s : 
            if isAlphanumeric(char) :
                stack.append(char)
    
        for char in s : 
            if isAlphanumeric(char) : 
                if char != stack.pop() : 
                    return False

        return True