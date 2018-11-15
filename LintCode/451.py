"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        node = head.next
        head.next = node.next
        node.next = head
        head = node
        node = node.next
        
        while node.next and node.next.next:
            next_node = node.next
            node.next = next_node.next
            next_node.next = node.next.next
            node.next.next = next_node
            node = node.next.next
        
        return head
