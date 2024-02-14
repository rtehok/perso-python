from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = [num for num in nums if num < 0]
        positives = [num for num in nums if num > 0]
        res = []
        for i in range(len(positives)):
            res.append(positives[i])
            res.append(negatives[i])

        return res


assert Solution().rearrangeArray([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]
assert Solution().rearrangeArray([-1, 1]) == [1, -1]
