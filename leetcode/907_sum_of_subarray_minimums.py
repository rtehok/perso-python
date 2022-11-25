from typing import List


class Solution:
    # O(n2)
    # def sumSubarrayMins(self, arr: List[int]) -> int:
    #     res = 0
    #     n = len(arr)
    #     for i in range(n):
    #         current_min = arr[i]
    #         for j in range(i, n):
    #             res += min(arr[i:j + 1])
    #
    #     return res
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        stack = []

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i
                count_sub_arrays = (mid - left_boundary) * (right_boundary - mid)
                contribution = count_sub_arrays * arr[mid]
                res += contribution
            stack.append(i)

        return res % MOD


if __name__ == "__main__":
    assert Solution().sumSubarrayMins([3, 1, 2, 4]) == 17
    assert Solution().sumSubarrayMins([11, 81, 94, 43, 3]) == 444
