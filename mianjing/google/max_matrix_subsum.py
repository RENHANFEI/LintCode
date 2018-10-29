def max_subarray(array):
    if not array:
        return 0

    presum = [0] * (len(array) + 1)
    for i, num in enumerate(array):
        presum[i + 1] = presum[i] + num

    max_subsum = array[0]
    min_presum = presum[0]
    for presum in presum[1:]:
        max_subsum = max(max_subsum, presum - min_presum)
        min_presum = min(min_presum, presum)

    return max_subsum

A = [-1,-2,1]
print(max_subarray(A))


def max_subsum_n2m_lowspace(matrix):
    if not matrix:
        return 0

    if not is_valid(matrix):
        raise Exception("Invalid Input!")

    max_sum = matrix[0][0]
    m, n = len(matrix), len(matrix[0])

    for top in range(m):
        rowsum = [0] * (m + 1)
        for down in range(top, m):
            min_sum = 0
            prefixsum = [0] * (m + 1)
            for y in range(n):
                rowsum[y] += matrix[down][y] 
                prefixsum[y + 1] =  prefixsum[y] + rowsum[y]
                max_sum = max(max_sum, prefixsum[y + 1] - min_sum)
                min_sum = min(min_sum, prefixsum[y + 1])
                
    return max_sum

def max_subsum_n2m(matrix):
    # write your code here
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    if n == 0:
        return 0

    presum = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + matrix[i - 1][j - 1]
    
    ans = matrix[0][0]
    for top in range(m):
        for bottom in range(top + 1, m + 1):
            subsum = 0
            for k in range(1, n + 1):
                diff = presum[bottom][k] - presum[top][k] - (presum[bottom][k - 1] - presum[top][k - 1])
                subsum += diff
                ans = max(ans, subsum)
                if subsum < 0:
                    subsum = 0
    return ans


def max_subsum_n2mk(matrix):
    if not matrix:
        return 0

    if not is_valid(matrix):
        raise Exception("Invalid Input!")

    max_sum = matrix[0][0]
    m, n = len(matrix), len(matrix[0])
    for start_y in range(n):
        for end_y in range(start_y, n):
            row_sum = [sum(matrix[x][start_y: end_y + 1]) for x in range(m)]
            max_sum = max(max_sum, max_subsum_1d(row_sum))

    return max_sum


def max_subsum_1d(array):
    if not array:
        return 0

    max_subsum = array[0]
    subsum = 0

    for num in array:
        if subsum < 0:
            subsum = num
        else:
            subsum += num

        if subsum > max_subsum:
            max_subsum = subsum

    return max_subsum



def max_subsum_m2n2(matrix):
    if not matrix:
        return 0

    if not is_valid(matrix):
        raise Exception("Invalid Input!")

    # traverse the matrix to get the maxsum
    max_sum = matrix[0][0]
    m, n = len(matrix), len(matrix[0])
    for start_x in range(m):    # O(M)
        for start_y in range(n):    # O(N)
            sub_sum = 0
            for end_x in range(start_x, m):   # O(M)
                for end_y in range(start_y, n):    # O(N)
                    sub_sum += matrix[end_x][end_y]
                    max_sum = max(max_sum, sub_sum)

    return max_sum


def max_subsum_m3n3(matrix):
    if not matrix:
        return 0

    if not is_valid(matrix):
        raise Exception("Invalid Input!")

    # traverse the matrix to get the maxsum
    max_sum = matrix[0][0]
    m, n = len(matrix), len(matrix[0])
    for start_x in range(m):    # O(M)
        for end_x in range(start_x, m):   # O(M)
            for start_y in range(n):    # O(N)
                for end_y in range(start_y, n):    # O(N)
                    sub_sum = calc_sub_sum(matrix, start_x, start_y, end_x, end_y)
                    max_sum = max(max_sum, sub_sum)

    return max_sum

def calc_sub_sum(matrix, start_x, start_y, end_x, end_y):
    sub_sum = 0
    for i in range(start_x, end_x + 1):    # O(M)
        for j in range(start_y, end_y + 1):    # O(N)
            sub_sum += matrix[i][j]
    return sub_sum


def is_valid(matrix):
    return True


tests = [
[[1, 2], [1, 3]],
[[1, -4], [1, 3]],
[[1, -4, 3], [-2, 0, 1], [5, -1, 1]],
[[-1, -1], [-1, -2]]
]

for test in tests:
    # print(max_subsum_m3n3(test))
    # print(max_subsum_m2n2(test))
    print(max_subsum_n2mk(test))
    print(max_subsum_n2m(test))