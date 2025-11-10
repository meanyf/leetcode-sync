class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        set2 = set(edges[0])
        common = [x for x in edges[1] if x in set2]
        return common[0]