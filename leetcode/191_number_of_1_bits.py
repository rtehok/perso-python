class Solution:
    def hammingWeight(self, n: int) -> int:
        # print("{0:b}".format(n))
        # return sum([(n & (1 << i)) != 0 for i in range(32)])
        res = 0
        while n != 0:
            res += n & 1
            n = n >> 1
            # print(n, "{0:b}".format(n))
        return res


if __name__ == "__main__":
    print(Solution().hammingWeight(5))
    print(Solution().hammingWeight(12))
    print(Solution().hammingWeight(42))
