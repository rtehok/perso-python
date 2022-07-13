from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """ Recursion + backtracking """
        # if not matchsticks:
        #     return False
        #
        # n = len(matchsticks)
        # perimeter = sum(matchsticks)
        # possible_side = perimeter // 4
        # matchsticks.sort(reverse=True)
        #
        # sides = [0] * 4
        #
        # def dfs(index):
        #     if index == n:
        #         return sides[0] == sides[1] == sides[2] == possible_side
        #
        #     for i in range(4):
        #         if sides[i] + matchsticks[index] <= possible_side:
        #             sides[i] += matchsticks[index]
        #             if dfs(index + 1):
        #                 return True
        #             sides[i] -= matchsticks[index]
        #     return False
        #
        # return dfs(0)
        """ DP + memoization """
        if not matchsticks:
            return False

        n = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side = perimeter // 4
        if possible_side * 4 != perimeter:
            return False

        memo = {}

        def helper(matchstick_used, sides_done):
            total = 0
            for i in range(n - 1, -1, -1):
                if not (matchstick_used & (1 << i)):
                    total += matchsticks[n - 1 - i]  # sum of length of used matchstick

            if total > 0 and total % possible_side == 0:
                sides_done += 1

            if sides_done == 3:
                return True

            if (matchstick_used, sides_done) in memo:
                return memo[(matchstick_used, sides_done)]  # use memoization

            ans = False

            c = total // possible_side
            remainder = possible_side * (c + 1) - total  # available space in the current side (incomplete)

            for i in range(n - 1, -1, -1):
                if matchsticks[n - 1 - i] <= remainder and matchstick_used & (1 << i):
                    if helper((matchstick_used ^ (1 << i)), sides_done):
                        ans = True
                        break

            memo[(matchstick_used, sides_done)] = ans
            return ans

        return helper((1 << n) - 1, 0)  # initial mask with all matchsticks available


if __name__ == "__main__":
    assert Solution().makesquare([1, 1, 2, 2, 2])
    assert not Solution().makesquare([3, 3, 3, 3, 4])
