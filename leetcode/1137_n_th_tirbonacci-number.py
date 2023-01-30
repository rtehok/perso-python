class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n

        if n == 2:
            return 1

        if n >= 3:
            a, b, c = 0, 1, 1
            for _ in range(3, n + 1, 1):
                tmp = a + b + c
                a = b
                b = c
                c = tmp

            return c


if __name__ == "__main__":
    assert Solution().tribonacci(4) == 4
    assert Solution().tribonacci(25) == 1389537
