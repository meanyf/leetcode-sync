class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        s = set(['a', 'e', 'i', 'o','u'])
        words = [x if x[0] in s and x[len(x) - 1] in s else 0 for x in words]
        prefix = [0] * (len(words) + 1)
        for i in range(1, len(words) + 1):
            prefix[i] = prefix[i - 1] + (1 if words[i - 1] else 0)
        return [prefix[end + 1] - prefix[start] for start, end in queries]