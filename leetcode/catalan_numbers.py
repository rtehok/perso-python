def bellNumber(n):
    dp = [[] for _ in range(n + 1)]

    dp[0].insert(0, 1)

    for i in range(1, n + 1):
        dp[i].insert(0, dp[i - 1][i - 1])

        for j in range(1, i + 1):
            dp[i].append(dp[i][j - 1] + dp[i - 1][j - 1])

    return dp


if __name__ == "__main__":
    print(bellNumber(5))
