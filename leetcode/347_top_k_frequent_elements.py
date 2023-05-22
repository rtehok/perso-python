import collections
import heapq
from typing import List


class Solution:
    def topKFrequentV1(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        return [k for k, v in list(sorted(d.items(), key=lambda item: item[1], reverse=True))][:k]

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = collections.Counter(nums).items()
        for num, freq in count:
            bucket[freq].append(num)
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]


if __name__ == "__main__":
    assert Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
    assert Solution().topKFrequent(nums=[1], k=1) == [1]
