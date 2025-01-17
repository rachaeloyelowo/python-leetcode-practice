class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_dict = { 
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" or char == "}" or char == "]":
                if stack and (stack[len(stack) - 1] == parenthesis_dict[char]):
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        return False
        