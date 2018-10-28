def f1(circle):
    friend_list = dict()
    for i, friends in enumerate(circle):
        friend_list[i] = []
        for j, friend in enumerate(friends):
            if friend and i != j: friend_list[i].append(j)
    return friend_list

def f3(circle):    # if all are in one friend circle
    if not circle:
        return True
    friend_list = f1(circle)
    connected = [False] * len(friend_list)    # to record whether the idx connected
    dfs(friend_list, 0, connected)
    for c in connected:
        if not c:
            return False
    return True

def dfs(friend_list, node, connected):
    friends = friend_list[node]
    for friend in friends:
        if not connected[friend]:
            connected[friend] = True
            dfs(friend_list, friend, connected)


circle1 = [[1,1,0],[1,1,1],[0,1,1]]
circle2 = [[1,0,1],[0,1,0],[1,0,1]]
print(f1(circle1))
print(f1(circle2))
print(f3(circle1))
print(f3(circle2))