from typing import List


class Solution:
    # O(3 ** n // 2)
    def tallestBillboardV1(self, rods: List[int]) -> int:
        def helper(half_rods):
            states = set()
            states.add((0, 0))

            # create all combination of rods
            # [1, 2, 3, 4]
            # (0, 0), (0, 1), (1, 0), (1 + 2, 0), (2, 0), (0, 2), (0, 2 + 1) => FIRST
            # (0, 0), (0, 3), (3, 0), (3 + 4, 0), (4, 0), (0, 4), (0, 4 + 3) => SECOND
            for rod in half_rods:
                new_states = set()
                for left, right in states:
                    new_states.add((left + rod, right))
                    new_states.add((left, right + rod))

                states |= new_states

            memo = {}
            # store key = diff, value = one of the 2 values
            for left, right in states:
                memo[left - right] = max(memo.get(left - right, 0), left)

            return memo

        n = len(rods)
        first = helper(rods[:n // 2])
        second = helper(rods[n // 2:])

        ans = 0

        # {-3: 0, -2: 0, -1: 1, 0: 0, 1: 2, 2: 2, 3: 3}
        # {-7: 0, -4: 0, -3: 0, -1: 3, 0: 0, 1: 4, 3: 3, 4: 4, 7: 7}
        # left should be equal to right, so diff should be opposite
        for diff in first:
            if -diff in second:
                ans = max(ans, first[diff] + second[-diff])

        return ans

    # TC O(n * m) / SC O(m)
    # m = maximum sum of rods
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for r in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                # Add rod to taller
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)

                # Add rod to shorter
                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)

            dp = new_dp

        return dp[0]


if __name__ == "__main__":
    assert Solution().tallestBillboard([1, 2, 3, 4]) == 5
    assert Solution().tallestBillboard([1, 2, 3, 6]) == 6
    assert Solution().tallestBillboard([1, 2, 3, 4, 5, 6]) == 10
    assert Solution().tallestBillboard([1, 2]) == 0
