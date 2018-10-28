def f1(matrix):
    break_flag = False
    for start_x, row in enumerate(matrix):
        for start_y, elem in enumerate(row):
            if elem == 0:
                break_flag = True
                break
        if break_flag: break

    x, y = start_x, start_y

    while x < len(matrix) and matrix[x][start_y] == 0: x += 1
    while y < len(matrix[0]) and row[y] == 0: y += 1

    return start_x, start_y, x - 1, y - 1


def f2(matrix):
    ans = []
    for start_x, row in enumerate(matrix):
        for start_y, elem in enumerate(row):
            if elem == 0:
                x, y = start_x, start_y
                while x < len(matrix) and matrix[x][start_y] == 0:
                    x += 1
                while y < len(matrix[0]) and row[y] == 0:
                    row[y] = 1
                    y += 1
                ans.append((start_x, start_y, x - 1, y - 1))

    return ans


def f3(matrix):
    ans = []
    for x, row in enumerate(matrix):
        for y, elem in enumerate(row):
            if elem == 0:
                component = []
                dfs(x, y, matrix, component)
                ans.append(component)

    return ans



def dfs(x, y, matrix, component):
    if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] == 0:
        matrix[x][y] = 1
        component.append((x,y))
        dfs(x + 1, y, matrix, component)
        dfs(x - 1, y, matrix, component)
        dfs(x, y + 1, matrix, component)
        dfs(x, y - 1, matrix, component)


in1 = [
[1,1,1,1,1,1], 
[1,1,1,1,1,1],
[1,1,1,1,1,1],
[1,1,1,1,1,1],
[1,0,0,1,1,1]
]

in2 = [
[1,1,1,1,1,1], 
[0,0,1,0,1,1],
[0,0,1,0,1,0],
[1,1,1,0,1,0],
[1,0,0,1,1,1]
]

in3 = [
[1,0,1,1,1,1], 
[0,0,1,0,1,1],
[0,0,1,0,1,0],
[1,1,1,0,1,0],
[1,0,0,1,1,1]
]

print(f1(in1))
print(f2(in2))
print(f3(in3))