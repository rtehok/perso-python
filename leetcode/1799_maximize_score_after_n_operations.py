import math
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        memo_size = 2 ** n
        memo = [-1] * memo_size

        def solve(mask, pair_picked):
            if 2 * pair_picked == n:
                return 0

            if memo[mask] != -1:
                return memo[mask]

            max_score = 0

            for first_index in range(n):
                for second_index in range(first_index + 1, n):
                    # if already picked or same numbers
                    if (mask >> first_index) & 1 == 1 or (mask >> second_index) & 1 == 1:
                        continue

                    new_mask = mask | (1 << first_index) | (1 << second_index)  # both indexes are marked as picked in new mask
                    curr_score = (pair_picked + 1) * math.gcd(nums[first_index], nums[second_index])
                    remaining_score = solve(new_mask, pair_picked + 1)
                    max_score = max(max_score, curr_score + remaining_score)
                    # next iteration will use mask, so we are backtracking

            memo[mask] = max_score  # current sub-problem
            return max_score

        return solve(0, 0)


if __name__ == "__main__":
    assert Solution().maxScore(nums=[3, 4, 6, 8]) == 11
    assert Solution().maxScore(nums=[1, 2]) == 1
    assert Solution().maxScore(nums=[1, 2, 3, 4, 5, 6]) == 14
