class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 0:
        #     return False
        #
        # if n % 2 == 0:
        #     return self.isPowerOfTwo(n // 2)
        #
        # return n == 1
        return n != 0 and n & (n - 1) == 0


if __name__ == "__main__":
    #   1
    # & 0
    # ----
    #   0
    assert Solution().isPowerOfTwo(1)
    #   10000
    # & 01111
    # ----
    #   00000
    assert Solution().isPowerOfTwo(16)
    #   11
    # & 01
    # ----
    #   01
    assert not Solution().isPowerOfTwo(3)
