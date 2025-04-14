class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        r = 0
        n = len(searchWord)
        N = len(sentence)
        idx = 1
        space = 0
        old_space = 0
        for i, ch in enumerate(sentence):
            if ch == ' ':
                idx += 1
                space = i + 1
                old_space = space
            if space < N and searchWord[r] == sentence[space]:
                r += 1
                space += 1
            else:
                r = 0
                space = old_space
            if r == n:
                return idx
        return -1