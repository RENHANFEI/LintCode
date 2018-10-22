"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if not head or not head.next:
            return head
            
        pre_node = None
        node = head
        
        while node:
            next_node = node.next
            node.next = pre_node
            if not next_node:
                return node
            pre_node = node
            node = next_node
