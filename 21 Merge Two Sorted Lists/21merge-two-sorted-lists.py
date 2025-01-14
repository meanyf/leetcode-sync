# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lst = None
        cur1 = list1
        cur2 = list2
        if cur1 is None:
            return cur2
        elif cur2 is None:
            return cur1
        
        if cur1.val <= cur2.val:
            lst = cur1
            cur1 = cur1.next
        else:
            lst = cur2
            cur2 = cur2.next
        lst_next = lst.next
        current = lst
        # last_lst = None
        # while current.next is not None:
        #     current = current.next
        while cur1 is not None or cur2 is not None:
            if cur1 is None:
                current.next = cur2
                current = current.next
                return lst
            elif cur2 is None:
                current.next = cur1
                current = current.next
                return lst    
            
            if cur1.val >= cur2.val:
                current.next = cur2
                current = current.next
                cur2 = cur2.next
            elif cur1.val < cur2.val:
                current.next = cur1
                current = current.next
                cur1 = cur1.next
        return lst    