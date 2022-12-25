import bisect
from typing import List


class Solution:
    def answerQueriesNaive(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        res = [0] * m

        for i, q in enumerate(queries):
            first = 0
            while first < n and nums[first] > q:
                first += 1

            if first == n:
                continue

            tmp = 0
            for num in sorted(nums[first:]):
                tmp += num
                if tmp <= q:
                    res[i] += 1
                else:
                    continue

        return res

    def answerQueriesGreedy(self, nums: List[int], queries: List[int]) -> List[int]:
        # "A subsequence is an array that can be derived from another array
        # by deleting some or no elements without changing the order of the remaining elements."
        # BUT it does not matter that doing 1 + 2 + 3 == 2 + 1 + 3 == 3 + 2 + 1 == 3 + 1 + 2 == ...
        nums.sort()
        res = []

        for query in queries:
            count = 0
            for num in nums:
                if query >= num:
                    query -= num
                    count += 1
                else:
                    break
            res.append(count)

        return res

    # Presum + binary search
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()

        # Create an array of preSum to have for each ith index, the sum up to the ith value (included)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        # do a binary search (bisect right)
        for query in queries:
            index = bisect.bisect_right(nums, query)
            res.append(index)

        return res


if __name__ == "__main__":
    assert Solution().answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21]) == [2, 3, 4]
    assert Solution().answerQueries(nums=[2, 3, 4, 5], queries=[1]) == [0]
