#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
        cur = dummy
        for _ in range(cnt - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
# @lc code=end

