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
        
        node = head
        smaller, s_smaller = None, None
        bigger, s_bigger = None, None
        equal, s_equal = None, None
        
        while node:
            if node.val > x:
                if bigger:
                    bigger.next = node
                    bigger = bigger.next
                else:
                    bigger = node
                    s_bigger = bigger
            if node.val < x:
                if smaller:
                    smaller.next = node
                    smaller = smaller.next
                else:
                    smaller = node
                    s_smaller = smaller
            else:
                if equal:
                    equal.next = equal
                    equal = equal.next
                else:
                    equal = node
                    s_equal = equal
            node = node.next
                    
        if smaller:
            if equal:
                smaller.next = s_equal
                equal.next = s_bigger
            else:
                smaller.next = s_bigger
            return s_smaller
            
        if equal:
            equal.next = s_bigger
            return s_equal
            
        return s_bigger
                    
        
        
sol = Solution()
