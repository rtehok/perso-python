class Solution:
    def checkRecordRecursive(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        def eligible_combinations(n, total_absences, consecutive_lates):
            if total_absences >= 2 or consecutive_lates >= 3:
                return 0

            if n == 0:
                return 1

            if memo[n][total_absences][consecutive_lates] != -1:
                return memo[n][total_absences][consecutive_lates]

            # Present
            cnt = eligible_combinations(n - 1, total_absences, 0)

            # Absent
            cnt += eligible_combinations(n - 1, total_absences + 1, 0)
            cnt %= MOD

            # Late
            cnt += eligible_combinations(n - 1, total_absences, consecutive_lates + 1)
            cnt %= MOD

            memo[n][total_absences][consecutive_lates] = cnt
            return cnt

        return eligible_combinations(n, 0, 0)

    def checkRecordTabulation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for length in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    # Present
                    dp[length + 1][total_absences][0] += dp[length][total_absences][consecutive_lates]
                    dp[length + 1][total_absences][0] %= MOD
                    # Absent
                    if total_absences < 1:
                        dp[length + 1][total_absences + 1][0] += dp[length][total_absences][consecutive_lates]
                        dp[length + 1][total_absences + 1][0] %= MOD
                    # Late
                    if consecutive_lates < 2:
                        dp[length + 1][total_absences][consecutive_lates + 1] += dp[length][total_absences][
                            consecutive_lates]
                        dp[length + 1][total_absences][consecutive_lates + 1] %= MOD

        cnt = 0
        for total_absences in range(2):
            for consecutive_lates in range(3):
                cnt += dp[n][total_absences][consecutive_lates]
                cnt %= MOD

        return cnt

    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp_curr = [[0] * 3 for _ in range(2)]
        dp_next = [[0] * 3 for _ in range(2)]
        dp_curr[0][0] = 1

        for _ in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    # Present
                    dp_next[total_absences][0] += dp_curr[total_absences][consecutive_lates]
                    dp_next[total_absences][0] %= MOD
                    # Absent
                    if total_absences < 1:
                        dp_next[total_absences + 1][0] += dp_curr[total_absences][consecutive_lates]
                        dp_next[total_absences + 1][0] %= MOD
                    # Late
                    if consecutive_lates < 2:
                        dp_next[total_absences][consecutive_lates + 1] += dp_curr[total_absences][consecutive_lates]
                        dp_next[total_absences][consecutive_lates + 1] %= MOD

            dp_curr = [row[:] for row in dp_next]
            dp_next = [[0] * 3 for _ in range(2)]

        cnt = 0
        for total_absences in range(2):
            for consecutive_lates in range(3):
                cnt += dp_curr[total_absences][consecutive_lates]
                cnt %= MOD

        return cnt


assert Solution().checkRecord(2) == 8
assert Solution().checkRecord(1) == 3
assert Solution().checkRecord(10101) == 183236316
