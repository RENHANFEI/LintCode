from collections import defaultdict

def f1(edges):
    nodes = set()
    parent_nums = defaultdict(lambda: 0)
    for parent, child in edges:
        nodes.add(parent)
        nodes.add(child)
        parent_nums[child] += 1
    zero_parent = set()
    one_parent = set()
    for node in nodes:
        if parent_nums[node] == 0:
            zero_parent.add(node)
            continue
        if parent_nums[node] == 1:
            one_parent.add(node)

    return zero_parent, one_parent

def f2(edges, node1, node2):
    parents_dict = defaultdict(lambda: [])
    for parent, child in edges:
        parents_dict[parent].append(child)
    ancestors1, ancestors2 = set(), set()
    get_ancestors(parents_dict, node1, ancestors1)
    get_ancestors(parents_dict, node2, ancestors2)
    return len(ancestors1 & ancestors2) > 0

def get_ancestors(parents_dict, node, ancestors):
    parents = parents_dict[node]
    for parent in parents:
        ancestors.add(parent)
        get_ancestors(parents_dict, parent, ancestors)

def f3(edges, node):
    parents_dict = defaultdict(lambda: [])
    for parent, child in edges:
        parents_dict[child].append(parent)
    length = 0
    max_info = [0, node]  # max_length, max_node
    dfs(parents_dict, node, 0, max_info)
    return max_info[1]

def dfs(graph, node, length, max_info):
    if length > max_info[0]:
        max_info[0], max_info[1] = length, node
    for parent in graph[node]:
        dfs(graph, parent, length + 1, max_info)

eg = [(1, 4), (1, 5), (2, 5), (3, 6), (6, 7)]
print(f1(eg))
print(f2(eg, 4, 6))
print(f3(eg, 5))