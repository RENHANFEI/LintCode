"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        
        if not node:
            x_node = ListNode(x)
            x_node.next = x_node
            return x_node
        
        if node.next == node:
            x_node = ListNode(x)
            node.next = x_node
            x_node.next = node
            return node
            
        n = node
        iter_flag = False
        while node.val == node.next.val:
            node = node.next
            if node.next == n:
                iter_flag = True
                break
                
        if iter_flag:
            x_node = ListNode(x)
            x_node.next = node.next
            node.next = x_node
            return node
        
        if x >= node.val:
            max_val = node.val
            
            while x >= node.next.val and node.next.val >= max_val:
                node = node.next
                max_val = node.val
                
            if node.val == max_val:  # x > all elements
                x_node = ListNode(x)
                x_node.next = node.next
                node.next = x_node
                return node
            else:
                x_node = ListNode(x)
                x_node.next = node.next
                node.next = x_node
                return node
        
        else:
            while node.val < node.next.val:
                node = node.next
            
            if node.next.val > x:  # node.next is min
                x_node = ListNode(x)
                x_node.next = node.next
                node.next = x_node
                return node
                
            else:
                while node.next.val < x:
                    node = node.next
                x_node = ListNode(x)
                x_node.next = node.next
                node.next = x_node
                return node
                
                
