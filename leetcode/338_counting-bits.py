from typing import List


class Solution:
    def countBitsDP(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

    def countBits(self, n: int) -> List[int]:
        power = 1
        p = 1
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == power:
                ans[i] = 1
                power <<= 1
                p = 1
            else:
                ans[i] = ans[p] + 1
                p += 1

        return ans


if __name__ == "__main__":
    assert Solution().countBits(2) == [0, 1, 1]
    assert Solution().countBits(3) == [0, 1, 1, 2]
    assert Solution().countBits(4) == [0, 1, 1, 2, 1]
    assert Solution().countBits(5) == [0, 1, 1, 2, 1, 2]
    assert Solution().countBits(6) == [0, 1, 1, 2, 1, 2, 2]
    assert Solution().countBits(7) == [0, 1, 1, 2, 1, 2, 2, 3]
    assert Solution().countBits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]
