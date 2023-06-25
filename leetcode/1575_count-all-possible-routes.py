from typing import List


class Solution:
    def countRoutesRecursive(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        memo = {}

        n = len(locations)

        def solve(curr_city, remaining_fuel):
            if remaining_fuel < 0:
                return 0

            if (curr_city, remaining_fuel) in memo:
                return memo[(curr_city, remaining_fuel)]

            ans = 0
            if curr_city == finish:
                ans = 1

            for next_city in range(n):
                if next_city != curr_city:
                    ans = (ans + solve(next_city,
                                       remaining_fuel - abs(locations[curr_city] - locations[next_city]))) % MOD

            memo[(curr_city, remaining_fuel)] = ans

            return ans

        return solve(start, fuel)

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        n = len(locations)
        # dp[i][j] contains the number of routes starting from i with j fuel
        # dp[i][j] is initialized with dp[finish][j] = 1 (one way to start from i = finish and go to finish)
        # to transition from k to i, reduce the fuel (j - abs(locations[k] - locations[i])) from k and add ways to reach finish to dp[i][j]
        dp = [[0] * (fuel + 1) for _ in range(n)]

        for j in range(fuel + 1):
            dp[finish][j] = 1

        for j in range(fuel + 1):
            for i in range(n):
                for k in range(n):
                    if i == k:
                        continue
                    if abs(locations[i] - locations[k]) <= j:
                        dp[i][j] = (dp[i][j] + dp[k][j - abs(locations[i] - locations[k])]) % MOD

        return dp[start][fuel]


if __name__ == "__main__":
    assert Solution().countRoutes(locations=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5) == 4
    assert Solution().countRoutes(locations=[4, 3, 1], start=1, finish=0, fuel=6) == 5
    assert Solution().countRoutes(locations=[5, 2, 1], start=0, finish=2, fuel=3) == 0
