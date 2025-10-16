class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = -float('inf')
        for item in sentences:
            mx = max(mx, len(item.split(' ')))
        return mx