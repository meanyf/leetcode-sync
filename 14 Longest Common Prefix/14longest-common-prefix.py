class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        mn = float('inf')
        for s in strs:
            if mn > len(s):
                mn = len(s)
        for i in range(mn):
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:mn]