class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_dict = {}
        score = []

        for i in range (len(operations)):
            if (operations[i] == "+" and len(score) > 1):
                score.append((score[len(score) - 1]) + (score[len(score) - 2]))
            elif (operations[i] == "D" and len(score) > 0):
                score.append(score[len(score) - 1]*2)
            elif (operations[i] == "C" and len(score) > 0):
                score.pop()
            else:

                score.append(int(operations[i]))

        
        total = 0
        for i in score:
            total += i
        return total