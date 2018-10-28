from collections import defaultdict

def f(tasks):
    indegrees = defaultdict(lambda: 0)
    tasks_dict = defaultdict(lambda: [])
    for before, after in tasks:
        if before not in indegrees:
            indegrees[before] = 0
        indegrees[after] += 1
        tasks_dict[before].append(after)

    zero_indegrees = []
    for node, indegree in indegrees.items():
        if indegree == 0:
            zero_indegrees.append(node)

    ans = []
    while zero_indegrees:
        task = zero_indegrees.pop()
        ans.append(task)
        for after in tasks_dict[task]:
            indegrees[after] -= 1
            if indegrees[after] == 0:
                zero_indegrees.append(after)

    return ans


tasks = [["cook", "eat"], ["study", "eat"], ["sleep", "study"]]
print(f(tasks))