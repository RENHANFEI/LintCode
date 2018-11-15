class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []

def f(root, deletions):
    if not root:
        return

    q = [root]
    ans = []

    if root.val not in deletions: 
        ans.append(root.val)

    while q:
        node = q.pop()
        children = node.children
        if node.val in deletions:
            for child in children:
                if child.val not in deletions:
                    ans.append(child.val)
        q.extend(children)

    return ans

#                 a
#        /     /     \      \
#      b      d      c      f
#   /   \   \
# h     z   i 

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
node_h = Node('h')
node_z = Node('z')
node_i = Node('i')

node_b.children.append(node_h)
node_b.children.append(node_z)
node_b.children.append(node_i)

node_a.children.append(node_b)
node_a.children.append(node_d)
node_a.children.append(node_c)
node_a.children.append(node_f)

deletions_list = [['b', 'f'], ['a', 'b'], ['b', 'h']]
for deletions in deletions_list:
    print(f(node_a, deletions))