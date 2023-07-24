from typing import List


class Solution:
    def findNumberOfLISBottomUp(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1] * n
        length = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = max(length)
        res = 0
        for i in range(n):
            if length[i] == max_length:
                res += count[i]

        return res

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * n
        length = [0] * n

        def dfs(i):
            if length[i] != 0:
                return

            length[i] = 1
            count[i] = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    dfs(j)
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = 0
        res = 0

        for i in range(n):
            dfs(i)
            max_length = max(max_length, length[i])

        for i in range(n):
            if length[i] == max_length:
                res += count[i]

        return res


if __name__ == "__main__":
    assert Solution().findNumberOfLIS([1, 3, 5, 4, 7]) == 2
    assert Solution().findNumberOfLIS([2, 2, 2, 2, 2]) == 5
