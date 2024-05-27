from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)

        def gte(val):
            start, end = 0, n - 1
            idx = n

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] >= val:
                    idx = mid
                    end = mid - 1
                else:
                    start = mid + 1

            return idx

        nums.sort()
        for i in range(1, n + 1):
            k = gte(i)
            if n - k == i:
                return i

        return -1

    def specialArrayPrefixSum(self, nums: List[int]) -> int:
        n = len(nums)

        freq = [0] * (n + 1)
        for num in nums:
            freq[min(num, n)] += 1

        num_gte = 0
        for i in range(n, 0, -1):
            num_gte += freq[i]
            if i == num_gte:
                return i

        return -1


assert Solution().specialArray([3, 5]) == 2
assert Solution().specialArray([0, 0]) == -1
assert Solution().specialArray([0, 4, 3, 0, 4]) == 3
