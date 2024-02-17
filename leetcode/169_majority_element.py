import collections
from typing import List


class SolutionV1:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        majority, maj_elt = 0, None
        cnt = 0
        for i, x in enumerate(nums):
            if i > 0 and nums[i - 1] < nums[i]:
                cnt = 0

            cnt += 1
            if majority < cnt:
                majority = cnt
                maj_elt = x

        return maj_elt


class Solution:
    def majorityElementV1(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1

        return candidate

    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]


if __name__ == "__main__":
    assert Solution().majorityElement([3, 2, 3]) == 3
    assert Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
