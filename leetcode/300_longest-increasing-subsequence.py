from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]

    def lengthOfLISV2(self, nums: List[int]) -> int:
        res = []

        # Look into res the index to replace
        def binarySearch(l, r, target):
            mid = (r - l) // 2 + l

            if l == r:
                return l

            if res[mid] == target:
                return mid
            elif res[mid] < target:
                return binarySearch(mid + 1, r, target)
            else:
                return binarySearch(l, mid, target)  # do not decrease right, because it might be in the solution

        for num in nums:
            if not res or res[-1] < num:
                res.append(num)
                continue

            i = binarySearch(0, len(res) - 1, num)

            res[i] = num

        return len(res)


if __name__ == "__main__":
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
