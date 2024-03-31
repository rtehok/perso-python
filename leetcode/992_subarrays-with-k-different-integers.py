import collections
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            freq = collections.defaultdict(int)
            start = 0
            ans = 0
            for end in range(len(nums)):
                freq[nums[end]] += 1
                while len(freq) > k:
                    freq[nums[start]] -= 1
                    if freq[nums[start]] == 0:
                        del freq[nums[start]]
                    start += 1
                ans += end - start + 1
            return ans

        return helper(nums, k) - helper(nums, k - 1)


assert Solution().subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2) == 7
assert Solution().subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3) == 3
