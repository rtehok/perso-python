import collections
from typing import List


class Solution:
    def countNicePairsTLE(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        rev = [int(str(num)[::-1]) for num in nums]
        n = len(nums)
        ans = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                ans += 1 if nums[i] + rev[j] == nums[j] + rev[i] else 0
                ans %= MOD

        return ans

    def countNicePairsV2(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        rev = [int(str(num)[::-1]) for num in nums]
        ans = 0

        dic = collections.defaultdict(int)
        for i, num in enumerate(nums):
            x = num - rev[i]
            ans = (ans + dic[x]) % MOD
            dic[x] += 1

        return ans

    def countNicePairs(self, nums: List[int]) -> int:
        arr = [num - int(str(num)[::-1]) for num in nums]

        ans = 0
        for cnt in collections.Counter(arr).values():
            ans += cnt * (cnt - 1) // 2  # count number of pairs possible with same cnt

        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    assert Solution().countNicePairs(nums=[42, 11, 1, 97]) == 2
    assert Solution().countNicePairs(nums=[13, 10, 35, 24, 76]) == 4
