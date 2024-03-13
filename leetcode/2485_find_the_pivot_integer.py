import math


class Solution:
    def pivotIntegerV1(self, n: int) -> int:
        prefix_sum = []
        suffix_sum = []
        previous = 0
        for i in range(1, n + 1):
            previous += i
            prefix_sum.append(previous)

        next_sum = 0
        for i in range(n, 0, -1):
            next_sum += i
            suffix_sum.append(next_sum)

        for i in range(len(prefix_sum)):
            if prefix_sum[i] == suffix_sum[n - 1 - i]:
                return i + 1

        return -1

    def pivotIntegerTwoPointers(self, n: int) -> int:
        left, right = 1, n
        sum_left, sum_right = left, right

        if n == 1:
            return n

        while left < right:
            if sum_left < sum_right:
                sum_left += left + 1
                left += 1
            else:
                sum_right += right - 1
                right -= 1
            if sum_left == sum_right and left + 1 == right - 1:
                return left + 1

        return -1

    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        pivot = int(math.sqrt(total_sum))

        return pivot if pivot * pivot == total_sum else -1


assert Solution().pivotInteger(8) == 6
assert Solution().pivotInteger(1) == 1
assert Solution().pivotInteger(4) == -1
