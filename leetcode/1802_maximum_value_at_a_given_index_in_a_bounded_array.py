class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def getSum(index, value):
            cnt = 0
            # arithmetic sum = (A[1] + A[n]) * len / 2

            # on left side
            # if value > index => [v - index, ..., v - 1, value] of size (index + 1)
            # else there is [1, 1, ..., 1] of size (index + 1 - value) + [1, 2, ..., value - 1, value]
            if value > index:
                cnt += (value + value - index) * (index + 1) // 2
            else:
                cnt += (index - value + 1) + (value + 1) * value // 2

            # on right side
            # if value >= n - index => [value, value - 1, ..., value - (n - 1 - index)] of size (n - index)
            # else there is [value, value - 1, ..., 2, 1] of size (value) + [1, 1, ..., 1] of size (n - index - value)

            if value >= n - index:
                cnt += (value + value - n + 1 + index) * (n - index) // 2
            else:
                cnt += (value + 1) * value // 2 + (n - index - value)

            return cnt - value  # value is counted twice

        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2  # avoid infinite loop because we are doing left = mid
            if getSum(index, mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    # 1, 2, 2, 1 ==> 6
    assert Solution().maxValue(n=4, index=2, maxSum=6) == 2
    # 2, 3, 2, 1, 1, 1 => 10
    assert Solution().maxValue(n=6, index=1, maxSum=10) == 3
