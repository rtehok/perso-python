class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # 8 = 15  1000: +(f(10000)-1) = 15
        # 7 = 5    111: +(f(1000)-1) -((f(100)-1) -(f(10)-1)) = 7 - 3 + 1 = 5
        # 6 = 4    110: +(f(1000)-1) -(f(100)-1) = 7 - 3 = 4
        # 5 = 6    101: +(f(1000)-1) -(f(10)-1) = 7 - 1 = 6
        # 4 = 7    100: +(f(1000)-1) = 7
        # 3 = 2     11: +(f(100)-1) -(f(10)-1) = 3 - 1 = 2
        # 2 = 3     10: +(f(100)-1) = 3
        # 1 = 1      1: +(f(10)-1) = 1
        steps = 0
        sign = 1
        for bit in reversed(range(31)):
            if n & (1 << bit) != 0:
                steps += sign * ((1 << (bit + 1)) - 1)
                sign *= -1

        return steps


if __name__ == "__main__":
    assert Solution().minimumOneBitOperations(3) == 2
    assert Solution().minimumOneBitOperations(6) == 4
