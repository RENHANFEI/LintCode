"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        
        if not head:
            return ListNode(1)
        
        carry = self.plusOneCarry(head)
        
        if carry == 1:
            node = ListNode(1, head)
            return node
            
        return head
    
    def plusOneCarry(self, node):
        if node.next:
            node.val += self.plusOneCarry(node.next)
        else:
            node.val += 1
            
        if node.val == 10:
            node.val = 0
            return 1
        else:
            return 0
