# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
        if n == cnt:
            return head.next
        cur = head
        while cnt - n > 1:
            cnt -= 1
            cur = cur.next
        
        cur.next = cur.next.next
        return head
        
