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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        if not head or not head.next or not head.next.next:
            return
        
        slow = head.next
        fast = head.next.next
        
        while slow != fast:
            if not fast.next or not fast.next.next:
                return
            slow = slow.next
            fast = fast.next.next
            
        slow2 = head
        while slow2 != slow:
            slow2 = slow2.next
            slow = slow.next
            
        return slow