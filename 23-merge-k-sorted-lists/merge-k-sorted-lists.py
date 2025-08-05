#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        res = dummy = ListNode()
        i = 0
        while i < len(lists):
            for j in range(len(lists)):
                # print(ans)
                if not lists[j]: 
                    lists[j] = -1
                    i += 1
                    continue
                if lists[j] == -1:
                    continue
                heapq.heappush(ans, lists[j].val)
                lists[j] = lists[j].next
            if len(ans) == len(lists):
                dummy.next = ListNode(heapq.heappop(ans))
                dummy = dummy.next
        while ans:
            dummy.next = ListNode(heapq.heappop(ans))
            dummy = dummy.next
        return res.next

        # ans = []
        # for item in lists:
        #     while item:
        #         ans.append(item.val)
        #         item = item.next
        # ans.sort()
        # res_tail = tail = ListNode()
        # for item in ans:
        #     tail.next = ListNode(item)
        #     tail = tail.next
        # return res_tail.next
# @lc code=end
