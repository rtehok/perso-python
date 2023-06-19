from typing import List


class Solution:
    def getAveragesV1(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        sub = []
        for i in range(n):
            if i - k < 0 or i + k >= n:
                res.append(-1)
            else:
                left = i - k
                right = i + k + 1
                if not sub:
                    s = sum(nums[left:right])
                else:
                    s -= nums[left - 1]
                    s += nums[right + 1]
                res.append(s // (right - left))

        return res

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n

        if k == 0:
            return nums

        if 2 * k + 1 > n:
            return res

        window_sum = sum(nums[:2 * k + 1])
        res[k] = window_sum // (2 * k + 1)

        for i in range(2 * k + 1, n):
            window_sum = window_sum - nums[i - (2 * k + 1)] + nums[i]
            res[i - k] = window_sum // (2 * k + 1)

        return res


if __name__ == "__main__":
    assert Solution().getAverages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3) == [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    assert Solution().getAverages(nums=[100000], k=0) == [100000]
    assert Solution().getAverages(nums=[8], k=100000) == [-1]
