# increasing paths in an array

def f1_3(array):    # O(N^2)
    if len(array) <= 1:
        return

    ans = []
    start_idx, idx = 0, 1
    prenum = array[start_idx]

    while idx < len(array):
        if array[idx] >= prenum:
            for i in range(start_idx, idx):
                ans.append(array[i:idx + 1])
        else:
            start_idx = idx
        prenum = array[idx]
        idx += 1

    return ans


def f1_2(array):    # O(N^2) search from start to end
    if len(array) <= 1:
        return

    ans = []    # a list of increasing arrays
    for start_idx in range(len(array) - 1):
        prenum = array[start_idx]
        idx = start_idx + 1
        subarray = [prenum]
        while idx < len(array) and array[idx] >= prenum:
            subarray.append(array[idx])
            ans.append(subarray[:])
            prenum = array[idx]
            idx += 1

    return ans



def f1(array):    # O(N^2) search from end to start
    if len(array) <= 1:
        return

    ans = []    # list of increasing arrays
    for end_idx in range(1, len(array)):
        last_num = array[end_idx]
        subarray = [last_num]
        idx = end_idx - 1
        while idx >= 0:
            num = array[idx]
            if num <= last_num:
                subarray.append(num)
                ans.append(list(reversed(subarray)))
                idx -= 1
                last_num = num
            else:
                break

    return ans

array = [1, 3, 4, 2, 6]
print(f1(array))
print(f1_2(array))
print(f1_3(array))


# increasing paths in a tree

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def f2(root):
    if not root or (not root.left and not root.right):
        return

    ans = []
    traverse(root, ans)

    return ans

def traverse(root, ans):    # O(N)
    valid_path(root, ans, [root.val])
    left, right = root.left, root.right
    if left: traverse(left, ans)
    if right: traverse(right, ans)


def valid_path(root, ans, path):    # O(logN ^2)
    left, right = root.left, root.right

    if left and left.val >= root.val:
        ans.append(path + [left.val])
        valid_path(left, ans, path + [left.val])

    if right and right.val >= root.val:
        ans.append(path + [right.val])
        valid_path(right, ans, path + [right.val])


def f2_2(root):
    if not root or (not root.left and not root.right):
        return

    ans = []
    get_paths(root, [root.val], ans)

    return ans

def get_paths(root, path, ans):
    left, right = root.left, root.right

    if left:
        if left.val >= path[-1]:
            valid_path_reversed = [left.val]
            for val in reversed(path):
                valid_path_reversed.append(val)
                ans.append(list(reversed(valid_path_reversed)))
            get_paths(left, path + [left.val], ans)
        else:
            get_paths(left, [left.val], ans)


    if right and right.val >= path[-1]:
        if right.val >= path[-1]:
            valid_path_reversed = [right.val]
            for val in reversed(path):
                valid_path_reversed.append(val)
                ans.append(list(reversed(valid_path_reversed)))
            get_paths(right, path + [right.val], ans)
        else:
            get_paths(right, [right.val], ans)


node_4 = Node(4)
node_5 = Node(5)
node_9 = Node(9)
node_3 = Node(3)
node_6 = Node(6)
node_8 = Node(8)
node_10 = Node(10)
node_4.left = node_5
node_4.right = node_9
node_5.left = node_3
node_5.right = node_6
node_9.left = node_8
node_9.right = node_10

print(f2(node_4))
print(f2_2(node_4))