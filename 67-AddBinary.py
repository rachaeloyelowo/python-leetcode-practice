class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_over = 0
        answer = ""

        while a or b : 
            add = carry_over
            carry_over = 0
            if a :
                add += int(a[-1])                
            if b :
                add += int(b[-1])

            if add > 1 :
                if add % 2 == 0 :
                    answer  = '0' + answer
                    carry_over = add // 2
                else : 
                    answer = '1' + answer
                    carry_over = add // 2
            else : 
                answer = str(add) + answer

            if a :
                a = a[:len(a) - 1]
            if b :
                b = b[:len(b) - 1]
                
        if carry_over :
            answer = str(carry_over) + answer

        return answer