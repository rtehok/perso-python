class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        a, b, = 0, 1

        for _ in range(2, n + 1):
            tmp = a + b
            a = b
            b = tmp

        return b


if __name__ == "__main__":
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
    assert Solution().fib(30) == 832040
