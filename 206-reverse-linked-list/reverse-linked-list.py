# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    g = None
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """ 
        if not head:
            return 
        if not head.next:
            return head
        
        h = self.reverseList(head.next)
        
        head.next = None
        cur = h
        while cur.next:
            cur = cur.next
        
        cur.next = head
        return h