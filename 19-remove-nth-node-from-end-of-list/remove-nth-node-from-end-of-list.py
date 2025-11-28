# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = dummy = ListNode()
        dummy.next = head
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1

        while cnt - n > 0:
            cnt -= 1
            dummy = dummy.next
        
        dummy.next = dummy.next.next
        return res.next
        
