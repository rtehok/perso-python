class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4

        return True


if __name__ == "__main__":
    assert not Solution().isPowerOfFour(8)
    assert not Solution().isPowerOfFour(2)
    assert not Solution().isPowerOfFour(-2147483648)
    assert not Solution().isPowerOfFour(17)
    assert Solution().isPowerOfFour(16)
    assert not Solution().isPowerOfFour(5)
    assert Solution().isPowerOfFour(1)
