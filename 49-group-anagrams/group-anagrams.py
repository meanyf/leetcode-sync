from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for item in strs:
            key = [0] * 26
            for i, ch in enumerate(item):
                key[ord(ch) - ord('a')] += 1
            d[tuple(key)].append(item)
        return list(d.values())