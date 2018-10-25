"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        i = 0
        node = head
        
        if m == n:
            return head
            
        pre_node = None
        reverse_start = None
        
        while node:
            i += 1
            next_node = node.next
            if i == m - 1:
                reverse_start = node
            if i == m:
                reverse_end = node
                pre_node = node
            if i > m and i < n:
                node.next = pre_node
                pre_node = node
            if i == n:
                node.next = pre_node
                reverse_end.next = next_node
                if reverse_start:
                    reverse_start.next = node
                else:
                    return node
            
            node = next_node
            
        return head
