import math
from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque()
        q.append((amount, 0))
        visited = set()
        visited.add(amount)

        if amount == 0:
            return 0

        while q:
            remainder, number_of_visit = q.popleft()

            for coin in coins:
                tmp = remainder - coin

                if tmp < 0 or tmp in visited:
                    continue

                if tmp > 0:
                    visited.add(tmp)
                    q.append((tmp, number_of_visit + 1))

                elif tmp == 0:
                    return number_of_visit + 1

        return -1

    def coinChangeDP(self, coins: List[int], amount: int) -> int:
        # dp[i] stores the min number of coins to make i amount
        dp = [math.inf] * (amount + 1)
        dp[0] = 0  # it takes 0 coin to make amount 0

        # solve subproblem
        for current_amount in range(1, amount + 1):
            for coin in coins:
                if current_amount >= coin:
                    dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

        return dp[amount] if dp[amount] != math.inf else -1


if __name__ == "__main__":
    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 3) == -1
    assert Solution().coinChange([1], 0) == 0
