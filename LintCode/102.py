"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if not head or not head.next or not head.next.next:
            return False
            
        slow = head.next
        fast = head.next.next
        
        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            if not fast.next:
                break
            else:
                fast = fast.next.next
            
        return False