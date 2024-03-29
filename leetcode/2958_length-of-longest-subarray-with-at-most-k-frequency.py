import collections
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = collections.Counter()
        ans = 0
        start = -1
        for end in range(len(nums)):
            freq[nums[end]] += 1
            while freq[nums[end]] > k:
                start += 1
                freq[nums[start]] -= 1
            ans = max(ans, end - start)

        return ans


assert Solution().maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2) == 6
assert Solution().maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1) == 2
assert Solution().maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4) == 4
