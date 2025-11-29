# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(l):
            prev = None
            while l:
                nxt = l.next
                l.next = prev
                prev = l
                l = nxt
            return prev

        head = cur = ListNode()
        add = 0
        prev = None
        while l1 or l2:
            ans = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            add = 0
            if ans > 9:
                ans = ans % 10
                add = 1
            cur.val = ans
            prev = cur
            cur.next = ListNode(1)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if not add:
            prev.next = None
        return head