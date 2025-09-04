class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for char in s:
            if char in par:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
    
                if par[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0