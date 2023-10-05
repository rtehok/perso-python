import collections
from typing import List


class Solution:
    def majorityElementV1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = collections.Counter(nums)
        res = []
        for k, v in cnt.items():
            if v > n / 3:
                res.append(k)

        return res

    # Boyer-Moore Majority vote algorithm
    def majorityElement(self, nums: List[int]) -> List[int]:
        # constraint on n / 3 => cannot have more than 2 candidates
        cnt1, cnt2, candidate1, candidate2 = 0, 0, None, None
        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1, cnt1 = num, 1
            elif cnt2 == 0:
                candidate2, cnt2 = num, 1
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1

        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1

        res = []

        if cnt1 > len(nums) // 3:
            res.append(candidate1)
        if cnt2 > len(nums) // 3:
            res.append(candidate2)

        return res


if __name__ == "__main__":
    assert Solution().majorityElement([1, 1, 2, 1, 2, 3, 3, 2, 2, 2, 1, 2, 2, 3, 2, 2]) == [2]
    assert Solution().majorityElement([3, 2, 3]) == [3]
    assert Solution().majorityElement([1]) == [1]
    assert Solution().majorityElement([1, 2]) == [1, 2]
