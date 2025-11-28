# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = l = dummy = ListNode(0, head)
        for _ in range(n):
            dummy = dummy.next
        while dummy.next:
            dummy = dummy.next
            l = l.next
        l.next = l.next.next
        return res.next
