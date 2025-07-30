class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for item in operations:
            if item == '++X' or item =='X++': res += 1
            if item == '--X' or item =='X--': res -= 1
        return res