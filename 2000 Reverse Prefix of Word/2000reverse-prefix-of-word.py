class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        lef = 0
        idx = 0
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break
        while lef < idx:
            word[lef], word[idx] = word[idx], word[lef]
            lef += 1
            idx -= 1
        return ''.join(word)