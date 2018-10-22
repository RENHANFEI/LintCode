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
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        
        nodes = [head]
        
        while head:
            nodes.append(head.next)
            head = head.next
        
        if n == len(nodes) - 1:
            return nodes[1]
        elif n == 1:
            nodes[-3].next = None
            return nodes[0]
        else:
            nodes[-n-2].next = nodes[-n]
            return nodes[0]