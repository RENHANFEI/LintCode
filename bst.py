class TreeNode(object):

    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right


def find_min(tree):
    if tree == None:
        return None

    if tree.left == None:
        return tree

    return find_min(tree.left)


def find_max(tree):
    if tree == None:
        return None

    if tree.right == None:
        return tree

    return find_max(tree.right)


def find(tree, key):
    if tree == None:
        return None

    if key > tree.element:
        return find(tree.right, key)

    if key < tree.element:
        return find(tree.left, key)

    return tree


def insert(tree, key):
    if tree == None:
        tree = TreeNode(key)

    if key > tree.element:
        tree.right = insert(tree.right, key)

    if key < tree.element:
        tree.left = insert(tree.left, key)

    return tree


def delete(tree, key):
    if tree == None:
        return None

    if key > tree.element:
        tree.right = delete(tree.right, key)

    elif key < tree.element:
        tree.left = delete(tree.left, key)

    else:
        # find the key
        if tree.left == tree.right == None:
            return None

        if tree.left == None:
            return tree.right

        if tree.right == None:
            return tree.left

        if tree.left != None and tree.right != None:
            alter = find_min(tree.right)
            alter.right = delete(alter.right, alter.element)
            alter.left = tree.left
            return alter

    return tree


def preorder_print(tree):
    if tree == None:
        return

    print(tree.element)
    preorder_print(tree.left)
    preorder_print(tree.right)


def inorder_print(tree):
    if tree == None:
        return

    inorder_print(tree.left)
    print(tree.element)
    inorder_print(tree.right)


def postorder_print(tree):
    if tree == None:
        return

    postorder_print(tree.left)
    postorder_print(tree.right)
    print(tree.element)


# instance
tree = TreeNode(5)  # initialize
insert(tree, 2) # insert
insert(tree, 8) 
insert(tree, 7)
insert(tree, 4)
insert(tree, 1)
insert(tree, 9)
insert(tree, 10)
print("after insertions")
print("min: %d, max: %d" % (find_min(tree).element,find_max(tree).element))
preorder_print(tree)
delete(tree, 8)
print("after deletions")
postorder_print(tree)

