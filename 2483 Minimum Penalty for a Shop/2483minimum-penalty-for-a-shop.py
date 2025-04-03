class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yes = no = 0
        n = len(customers)
        answer = [0] * (n + 1)
        for i, s in enumerate(customers):
            answer[i] = no
            if s == 'N':
                no += 1
            else:
                yes += 1
        answer[-1] = no
        for i, s in enumerate(customers):
            answer[i] += yes
            if s == 'Y':
                yes -= 1
        return answer.index(min(answer))