#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        indexed_items = []
        def bin_search(lst):
            lo = 0
            hi = len(lst) - 1
            while lo <= hi:
                mi = (lo + hi) // 2
                if lst[mi] == 1:
                    lo = mi + 1
                else:
                    hi = mi - 1
            return lo

        prev = None
        for i, a in enumerate(mat):
            a_cnt = bin_search(a)
            indexed_items.append((i, a_cnt))
     
        indexed_items.sort(key = lambda x: x[1])
        print(indexed_items)
        return [x[0] for x in indexed_items][:k]
# @lc code=end

