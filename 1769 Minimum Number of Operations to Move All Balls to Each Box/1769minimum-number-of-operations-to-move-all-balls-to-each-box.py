class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        lst = list(map(int, list(boxes)))
        idxlst = [i for i, x in enumerate(lst) if x == 1]
        print(idxlst)
        answer = [0] * len(lst)
        for i, item in enumerate(lst):
            res = 0
            for num in idxlst:
                res += abs(num - i)
            answer[i] = res
        return answer