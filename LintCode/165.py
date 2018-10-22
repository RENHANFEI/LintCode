"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        
        if not l2:
            return l1
            
        if l1.val <= l2.val:
            h = l1
            l1 = l1.next
            if not l1:
                h.next = l2
        else:
            h = l2
            l2 = l2.next
            if not l2:
                h.next = l1
            
        l = h
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l = l.next
                l1 = l1.next
                if not l1:
                    l.next = l2
            else:
                l.next = l2
                l = l.next
                l2 = l2.next
                if not l2:
                    l.next = l1
                
        return h
        
