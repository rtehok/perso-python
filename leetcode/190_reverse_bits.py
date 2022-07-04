class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n & (1 << i):  # if at ith position, value is 1
                res |= 1 << (31 - i)  # set 1 to 31 - ith position

        return res


if __name__ == "__main__":
    # 00000010100101000001111010011100 ==> 00111001011110000010100101000000
    assert Solution().reverseBits(43261596) == 964176192
    # 11111111111111111111111111111101 ==> 10111111111111111111111111111111
    assert Solution().reverseBits(4294967293) == 3221225471
