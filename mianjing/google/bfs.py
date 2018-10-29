from collections import deque

def traverse():
    graph = dict()
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    ans = []
    bfs(graph, deque(["you"]), ans)
    print(ans)

def bfs(graph, q, ans):
    if not q:
        return
    node = q.popleft()
    ans.append(node)
    for connected_node in graph[node]:
        q.append(connected_node)
    bfs(graph, q, ans)

traverse()