from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        n = len(nums)

        i = 0
        start = 0

        while i < n:
            while i <= n - 2 and nums[i + 1] - nums[i] == 1:
                i += 1

            if start == i:
                res.append(f"{nums[start]}")
            else:
                res.append(f"{nums[start]}->{nums[i]}")

            i += 1
            start = i

        return res


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
