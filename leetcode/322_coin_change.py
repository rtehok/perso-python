from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque()
        q.append((amount, 0))
        visited = [0] * (amount + 1)

        if amount == 0:
            return 0

        while q:
            # print(q)
            remainder, number_of_visit = q.popleft()
            # print(visited[:amount + 1])

            for coin in coins:
                tmp = remainder - coin
                # print(remainder, coin, tmp)

                if tmp < 0 or visited[tmp] != 0:
                    continue

                if tmp > 0:
                    visited[tmp] = number_of_visit + 1
                    q.append((tmp, number_of_visit + 1))

                elif tmp == 0:
                    return number_of_visit + 1

        return -1


if __name__ == "__main__":
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([2], 3))
    print(Solution().coinChange([1], 0))
