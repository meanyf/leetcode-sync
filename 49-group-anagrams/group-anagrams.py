from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for item in strs:
            d[tuple(sorted(item))].append(item)
        return list(d.values())