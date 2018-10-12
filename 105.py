"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        
        if not head:
            return None
        
        h = head
        
        while head:
            node = RandomListNode(head.label)
            head.next, node.next = node, head.next
            head = node.next
        
        
        head = h
        a = ans = head.next
        
        while head: # connect random
            ans.random = head.random.next if head.random else None
            head = ans.next
            ans = head.next if head else None
        
        head = h
        ans = a
        
        while head: # connect next
            head.next = ans.next
            head = head.next
            ans.next = head.next if head else None
            ans = ans.next
            
        return a



# class Solution:
#     # @param head: A RandomListNode
#     # @return: A RandomListNode
#     def copyRandomList(self, head):
#         import copy
#         return copy.deepcopy(head)