# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        prev = None
        ex = True
        while head and ex:
            if prev is not None and prev.val == head.val:
                prev.next = head.next
                head = prev
                prev = prev.next
            prev = head
            head = head.next
            
        return res