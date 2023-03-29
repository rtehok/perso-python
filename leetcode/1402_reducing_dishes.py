from typing import List


class Solution:
    # O(n2) / O(1)
    def maxSatisfactionV1(self, satisfaction: List[int]) -> int:
        res = 0
        satisfaction.sort()

        if satisfaction[-1] < 0:
            return res

        n = len(satisfaction)

        for i in range(n):
            tmp = 0
            for j in range(i, n):
                tmp += (j - i + 1) * satisfaction[j]
                res = max(res, tmp)

        return res

    # Top down DP
    # O(n2) / O(n2)
    def maxSatisfactionTopDownDP(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def findMax(index, time):
            if index == n:
                return 0

            if memo[index][time] != -1:
                return memo[index][time]

            memo[index][time] = max(satisfaction[index] * time + findMax(index + 1, time + 1),
                                    findMax(index + 1, time))

            return memo[index][time]

        return findMax(0, 1)

    # Bottom-up DP
    # O(n2) / O(n2)
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[0] * (n + 2) for _ in range(n + 1)]  # bottom up, so dp rows is n + 1 long, time is shifted by 1

        for i in range(n - 1, -1, -1):  # starts at n - 1
            for time in range(1, n + 1):  # shift by 1
                dp[i][time] = max(satisfaction[i] * time + dp[i + 1][time + 1], dp[i + 1][time])

        return dp[0][1]

    # O(n * log(n)) / O(log(n))
    def maxSatisfactionGreedy(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        n = len(satisfaction)

        max_satisfaction = 0
        suffix_sum = 0

        for i in range(n - 1, -1, -1):
            if suffix_sum + satisfaction[i] > 0:
                suffix_sum += satisfaction[i]
                max_satisfaction += suffix_sum
            else:
                return max_satisfaction

        return max_satisfaction


if __name__ == "__main__":
    assert Solution().maxSatisfaction(satisfaction=[-1, -8, 0, 5, -9]) == 14
    assert Solution().maxSatisfaction(satisfaction=[4, 3, 2]) == 20
    assert Solution().maxSatisfaction(satisfaction=[-1, -4, -5]) == 0
    assert Solution().maxSatisfaction(satisfaction=[-2, 5, -1, 0, 3, -3]) == 35
