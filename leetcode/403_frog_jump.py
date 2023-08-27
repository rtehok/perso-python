from typing import List


class Solution:
    def canCrossTopDown(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[-1] * n for _ in range(n)]
        mark = dict((stones[i], i) for i in range(n))

        def solve(i, prev):
            if i == n - 1:
                return True

            if dp[i][prev] != -1:
                return dp[i][prev]

            ans = False

            for next_jump in [prev - 1, prev, prev + 1]:
                if next_jump > 0 and stones[i] + next_jump in mark:
                    ans |= solve(mark[stones[i] + next_jump], next_jump)

            dp[i][prev] = ans

            return ans

        return solve(0, 0)

    def canCrossBottomUp(self, stones: List[int]) -> bool:
        n = len(stones)
        mark = dict((stones[i], i) for i in range(n))
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = True

        for i in range(n):
            for prev in range(n - 1):
                if dp[i][prev]:
                    for x in [-1, 0, 1]:
                        if stones[i] + prev + x in mark:
                            dp[mark[stones[i] + prev + x]][prev + x] = True
        for i in range(n):
            if dp[-1][i]:
                return True

        return False

    def canCross(self, stones: List[int]) -> bool:
        jump_dict = {stone: set() for stone in stones}
        jump_dict[0].add(0)

        for stone in stones:
            for jump in jump_dict[stone]:
                for next_jump in range(jump - 1, jump + 2):
                    if next_jump > 0 and stone + next_jump in jump_dict:
                        jump_dict[stone + next_jump].add(next_jump)

        return bool(jump_dict[stones[-1]])


if __name__ == "__main__":
    assert Solution().canCross(stones=[0, 1, 3, 5, 6, 8, 12, 17])
    assert not Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11])
