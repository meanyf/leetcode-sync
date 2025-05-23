# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res = []
        while head:
            res.append(ListNode(head.val))
            head = head.next
        ans = head = res.pop()
        res.reverse()
        for item in res:
            head.next = item
            head = head.next
        return ans
