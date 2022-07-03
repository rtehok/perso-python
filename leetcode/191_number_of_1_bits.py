class Solution:
    def hammingWeight(self, n: int) -> int:
        # print("{0:b}".format(n))
        # return sum([(n & (1 << i)) != 0 for i in range(32)])
        res = 0
        while n != 0:
            res += n & 1  # count if rightmost digit is 1
            n = n >> 1  # shift right
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
