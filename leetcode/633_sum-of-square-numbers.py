import math


class Solution:
    def judgeSquareSumTLE(self, c: int) -> bool:
        a = 0
        while a ** 2 <= c:
            b = 0
            while b ** 2 <= c:
                if a ** 2 + b ** 2 == c:
                    return True
                b += 1
            a += 1
        return False

    def judgeSquareSumSqrt(self, c: int) -> bool:
        a = 0
        while a ** 2 <= c:
            b = math.sqrt(c - a ** 2)
            if b == int(b):
                return True
            a += 1
        return False

    def judgeSquareSum(self, c: int) -> bool:
        def binarySearch(start, end, target):
            if start > end:
                return False
            mid = start + (end - start) // 2
            if mid ** 2 == target:
                return True
            if mid ** 2 > target:
                return binarySearch(start, mid - 1, target)
            return binarySearch(mid + 1, end, target)

        a = 0
        while a ** 2 <= c:
            b = c - a ** 2
            if binarySearch(0, b, b):
                return True
            a += 1
        return False


assert Solution().judgeSquareSum(5)
assert not Solution().judgeSquareSum(3)
