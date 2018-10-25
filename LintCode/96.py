"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        if not head:
            return
        
        smaller, s_smaller = None, None
        bigger, s_bigger = None, None
        
        while head:
            if head.val >= x:
                if bigger:
                    bigger.next = head
                    bigger = bigger.next
                else:
                    bigger = head
                    s_bigger = bigger
            else:
                if smaller:
                    smaller.next = head
                    smaller = smaller.next
                else:
                    smaller = head
                    s_smaller = smaller
            head = head.next
        
        if s_bigger:
            bigger.next = None
                
        if smaller:
            smaller.next = s_bigger
            return s_smaller
        
        return s_bigger