# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        cur = head
        
        slow = fast = head
        cur = head
        prev = None
        next_ = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        
        if fast:
            slow = slow.next

        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True