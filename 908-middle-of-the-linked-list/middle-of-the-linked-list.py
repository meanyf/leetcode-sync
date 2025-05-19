# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
        cnt //= 2
        cur = head
        while cnt:
            cur = cur.next
            cnt -= 1
        return cur