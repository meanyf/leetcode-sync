#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res= dummy
        add = 0
        head = l1
        while l1 or l2:
            ans = 0
            ans += l1.val if l1 else 0
            ans += l2.val if l2 else 0
            ans += add
            val = 0
            if ans >= 10:
                val = ans - 10
                add = 1
            else:
                val = ans
                add = 0
            dummy.next = ListNode(val)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if add == 1:
            dummy.next = ListNode(1)

        return res.next
# @lc code=end

