import collections
from typing import List


class Solution:
    def maxSlidingWindowTLE(self, nums: List[int], k: int) -> List[int]:
        res = [max(nums[:k])]

        for i in range(1, len(nums) - k + 1):
            res.append(max(nums[i:i + k]))

        return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()  # pop the last one

            q.append(i)

        res = [nums[q[0]]]

        for i in range(k, len(nums)):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()  # pop to the right

            q.append(i)
            res.append(nums[q[0]])

        return res


if __name__ == "__main__":
    assert Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]
    assert Solution().maxSlidingWindow(nums=[1], k=1) == [1]
