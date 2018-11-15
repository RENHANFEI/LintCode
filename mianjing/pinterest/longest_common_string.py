def longest_common_string(A, B):

    m = len(A)
    n = len(B)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    ans = 0, 0    # longest length, end idx at A

    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                if dp[i + 1][j + 1] > ans[0]:
                    ans = dp[i + 1][j + 1], i

    return A[ans[1] - ans[0] + 1:ans[1] + 1]

A = "ABCD"
B = "CBCE"

A = ""
B = ""

print(longest_common_string(A, B))