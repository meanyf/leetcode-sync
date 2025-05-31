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
        cnt = 0
        while fast and fast.next:
            slow = slow.next
            cnt += 1
            fast = fast.next.next
        
        if fast:
            slow = slow.next

        cur = head
        prev = None
        next_ = None
        
        while cnt and cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
            cnt -= 1

        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True