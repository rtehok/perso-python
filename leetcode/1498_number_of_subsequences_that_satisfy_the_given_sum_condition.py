from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        ans = 0

        i, j = 0, n - 1

        while i <= j:
            if nums[i] + nums[j] <= target:
                ans = (ans + pow(2, j-i, MOD)) % MOD
                # ans += 2 ** (j - i)
                # ans %= MOD
                i += 1
            else:
                j -= 1

        return ans


if __name__ == "__main__":
    assert Solution().numSubseq(nums=[3, 5, 6, 7], target=9) == 4
    assert Solution().numSubseq(nums=[3, 3, 6, 8], target=10) == 6
    assert Solution().numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12) == 61