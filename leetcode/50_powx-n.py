import math


class Solution:
    def myPowV1(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n > 0:
            res = x
            n -= 1
            while n > 0:
                res *= x
                n -= 1
        else:
            if x == 0:
                return 0
            else:
                res = 1 / x
            n += 1
            while n < 0:
                res /= x
                n += 1
        return res

    def myPowV2(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPowV2(x, -n)

        return x * self.myPowV2(x, n - 1)

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 1:  # is odd
            return x * self.myPow(x * x, (n - 1) // 2)
        else:
            return self.myPow(x * x, n // 2)


if __name__ == "__main__":
    assert Solution().myPow(2.0, 10) == 1024.0
    assert Solution().myPow(x=2.10000, n=3) == math.pow(2.1, 3)
    assert Solution().myPow(x=2.00000, n=-2) == 0.25
