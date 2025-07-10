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
        cur = head
        cnt = 0
        last = None
        while cur:
            last = cur
            cur = cur.next
            cnt += 1
        cur = head
        if n == cnt:
            return cur.next
        cur = head
        for _ in range(cnt - n - 1):
            cur = cur.next
        fr = cur
        cur = head
        for _ in range(cnt - n + 1):
            if cur:
                cur = cur.next
        to = cur
        if fr:
            fr.next = to
        return head
# @lc code=end

