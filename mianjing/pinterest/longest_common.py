def longest_continuous_common_history(user1, user2):
    m, n = len(user1), len(user2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    max_i = 0
    for i in range(m):
        for j in range(n):
            if user1[i] == user2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                if dp[i + 1][j + 1] > max_length:
                    max_length = dp[i + 1][j + 1]
                    max_i = i + 1

    return user1[max_i - max_length:max_i]

user0 = [ "/start.html", "/pink.php", "/register.asp", "/orange.html", "/red.html" ]
user1 = [ "/red.html", "/green.html", "/blue.html", "/pink.php", "/register.asp" ]
user2 = [ "/start.html", "/green.html", "/blue.html", "/pink.php", "/register.asp", "/orange.html" ]
user3 = [ "/blue.html", "/logout.php" ]

print(longest_continuous_common_history(user0, user2))
print(longest_continuous_common_history(user1, user2))
print(longest_continuous_common_history(user0, user3))
print(longest_continuous_common_history(user1, user3))