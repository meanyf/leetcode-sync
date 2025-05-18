# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        s = ''.join(str(x) for x in res)
        return int(s, 2)
