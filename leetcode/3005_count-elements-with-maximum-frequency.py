import collections
from typing import List


class Solution:
    def maxFrequencyElementsV1(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        max_freq = 0
        for x, freq in cnt.items():
            max_freq = max(max_freq, freq)
        return sum(freq for _, freq in cnt.items() if freq == max_freq)

    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = {}
        total_freq = 0
        max_freq = 0

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

            freq = freqs[num]

            if freq > max_freq:
                max_freq = freq
                total_freq = freq
            elif freq == max_freq:
                total_freq += freq

        return total_freq


assert Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4]) == 4
assert Solution().maxFrequencyElements([1, 2, 3, 4, 5]) == 5
