class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # state 0:
        # 0
        # 0
        # state 1:
        # 1
        # 0
        # state 2:
        # 0
        # 1
        # state 3:
        # 1
        # 1
        def makeState(t1, t2):
            # if not t1 and not t2:
            #     return 0
            # if t1 and not t2:
            #     return 1
            # if not t1 and t2:
            #     return 2
            # return 3

            state = 0
            if t1:
                state |= 1  # 01 in binary
            if t2:
                state |= 2  # 10 in binary
            return state

        dp = [[None] * 4 for _ in range(n)]  # n rows * 4 columns to have dp[i][state]

        # i  | i + 1
        # ----------
        # t1 | t3
        # -- | -----
        # t2 | t4
        # Free: True, Blocked: False
        def helper(i, t1, t2):
            if i == n:
                return 1

            state = makeState(t1, t2)
            if dp[i][state] is not None:
                # use history here
                return dp[i][state]

            count = 0

            t3, t4 = i + 1 < n, i + 1 < n  # t3 == t4 but left as-is for comprehension, instead of having one variable

            if t1 and t2 and t3:  # All is free, try to place a tromino at t1, t2, t3
                count += helper(i + 1, False, True)  # next iteration t1 is blocked, t2 is free
            if t1 and t2 and t4:  # All is free, try to place a tromino at t1, t2, t4
                count += helper(i + 1, True, False)  # next iteration t1 is free, t2 is blocked
            if t1 and not t2 and t3 and t4:  # t2 blocked, can place tromino in t1, t3, t4 (no gap)
                count += helper(i + 1, False, False)  # next iteration t1 is blocked, t2 is blocked
            if not t1 and t2 and t3 and t4:  # t1 blocked, can place tromino in t2, t3, t4 (no gap)
                count += helper(i + 1, False, False)  # next iteration t1 is blocked, t2 is blocked
            if t1 and t2:  # try to place a vertical domino
                count += helper(i + 1, True, True)  # next iteration t1 is free, t2 is free
            if t1 and t2 and t3 and t4:  # all tiles are free, can fill all horizontally
                count += helper(i + 1, False, False)  # next iteration t1 is blocked, t2 is blocked
            if t1 and not t2 and t3:  # try to place a single horizontal domino when t2 is blocked
                count += helper(i + 1, False, True)  # next iteration t1 is blocked, t2 is free
            if not t1 and t2 and t4:  # try to place a single horizontal domino when t1 is blocked
                count += helper(i + 1, True, False)  # next iteration t1 is free, t2 is true
            if not t1 and not t2:  # neither t1 nor t2 are free (after 2 horizontal dominos for example)
                count += helper(i + 1, True, True)  # next iteration t1 is free, t2 is free

            dp[i][state] = count % MOD

            return dp[i][state]

        return helper(0, True, True)


if __name__ == "__main__":
    assert Solution().numTilings(1) == 1
    assert Solution().numTilings(2) == 2
    assert Solution().numTilings(3) == 5
    assert Solution().numTilings(4) == 11
