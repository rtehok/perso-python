class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a = 1
        b = 2

        for _ in range(2, n):
            tmp = a + b
            a = b
            b = tmp

        return b


if __name__ == "__main__":
    # 1 + 1
    # 2
    assert Solution().climbStairs(2) == 2
    # 1 + 1 + 1
    # 1 + 2
    # 2 + 1
    assert Solution().climbStairs(3) == 3
    # 1 + 1 + 1 + 1
    # 1 + 1 + 2
    # 1 + 2 + 1
    # 2 + 1 + 1
    # 2 + 2
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(38) == 63245986
