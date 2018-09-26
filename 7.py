"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if root == None:
            content = "[]"
        
        else:
            content = "["
            
            nodes = [root]
            while not (None in nodes and len(set(nodes)) == 1):
                node = nodes.pop(0)
                if node == None:
                    content += "None"
                else:
                    content += str(node.val)
                
                content += ','
                
                if node == None:
                    nodes.append(None)
                    nodes.append(None)
                else:
                    nodes.append(node.left)
                    nodes.append(node.right)
            
            content = content[:-1] + "]"  # delete the last ','
        
        with open("serialization", 'w') as f:
            f.write(content)
        
        return f
                

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        with open("serialization", 'r') as f:
            content = f.read()
            
        nodes = eval(content)
        
        if len(nodes) == 0:
            return
        
        treenodes = [None] * len(nodes)
        treenodes[0] = TreeNode(nodes[0])
        for i in range(len(nodes) - 1):
            if 2 * i + 1 < len(nodes) and nodes[2 * i + 1] != None:
                treenodes[2 * i + 1] = TreeNode(nodes[2 * i + 1])
                treenodes[i].left = treenodes[2 * i + 1]
            if 2 * i + 2 < len(nodes) and nodes[2 * i + 2] != None:
                treenodes[2 * i + 2] = TreeNode(nodes[2 * i + 2])
                treenodes[i].right = treenodes[2 * i + 2]
        
        return treenodes[0]
