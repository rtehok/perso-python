import functools


class Solution:
    def knightDialerTopDown(self, n: int) -> int:
        next_move = {
            1: {6, 8},
            2: {7, 9},
            3: {4, 8},
            4: {3, 9, 0},
            5: {},
            6: {1, 7, 0},
            7: {2, 6},
            8: {1, 3},
            9: {2, 4},
            0: {4, 6}
        }

        @functools.cache
        def dfs(i, n):
            if n == 0:
                return 1

            cnt = 0
            for neighbor in next_move[i]:
                cnt += dfs(neighbor, n - 1)

            return cnt

        ans = 0
        for i in range(10):
            ans += dfs(i, n - 1)
            ans %= (10 ** 9 + 7)

        return ans

    def knightDialerBottomUp(self, n: int) -> int:
        next_move = {
            1: {6, 8},
            2: {7, 9},
            3: {4, 8},
            4: {3, 9, 0},
            5: {},
            6: {1, 7, 0},
            7: {2, 6},
            8: {1, 3},
            9: {2, 4},
            0: {4, 6}
        }

        MOD = 10 ** 9 + 7
        dp = [[0] * 10 for _ in range(n)]
        for square in range(10):
            dp[0][square] = 1

        for remain in range(1, n):
            for square in range(10):
                ans = 0
                for next_square in next_move[square]:
                    ans += dp[remain - 1][next_square]
                    ans %= MOD
                dp[remain][square] = ans

        ans = 0
        for square in range(10):
            ans += dp[-1][square]
            ans %= MOD

        return ans

    def knightDialerBUSO(self, n: int) -> int:
        next_move = {
            1: {6, 8},
            2: {7, 9},
            3: {4, 8},
            4: {3, 9, 0},
            5: {},
            6: {1, 7, 0},
            7: {2, 6},
            8: {1, 3},
            9: {2, 4},
            0: {4, 6}
        }

        MOD = 10 ** 9 + 7
        dp = [0] * 10
        dp_prev = [1] * 10

        for remain in range(1, n):
            dp = [0] * 10
            for square in range(10):
                ans = 0
                for next_square in next_move[square]:
                    ans += dp_prev[next_square]
                    ans %= MOD
                dp[square] = ans

            dp_prev = dp

        ans = 0
        for square in range(10):
            ans += dp_prev[square]
            ans %= MOD

        return ans

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        # A B A
        # C E C
        # A B A
        #   D

        A = 4
        B = 2
        C = 2
        D = 1
        MOD = 10 ** 9 + 7

        for _ in range(n - 1):
            # from B => 2 ways to reach A
            # from C => 2 ways to reach A
            # from A => 1 way to reach B
            # from A => 1 way to reach C
            # from D => 2 way to reach C
            # from C => 1 way to reach D
            A, B, C, D = (2 * B + 2 * C), A, A + 2 * D, C

        return (A + B + C + D) % MOD


if __name__ == "__main__":
    assert Solution().knightDialer(1) == 10
    assert Solution().knightDialer(2) == 20
    assert Solution().knightDialer(3131) == 136006598
