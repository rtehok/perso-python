class Solution:
    def hammingWeightV1(self, n: int) -> int:
        return str(bin(n)[2:]).count("1")

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += n & 1
            n >>= 1
        return res


if __name__ == "__main__":
    #   101
    # & 001
    # -----
    #   001

    #   10
    # & 01
    # ----
    #   00

    #   1
    # & 1
    # ----
    #   1
    assert Solution().hammingWeight(5) == 2
    assert Solution().hammingWeight(12) == 2
    assert Solution().hammingWeight(42) == 3
    assert Solution().hammingWeight(11) == 3
