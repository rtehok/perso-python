class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if c & 1:
                ans += 0 if ((a & 1) or (b & 1)) else 1
            else:
                ans += (a & 1) + (b & 1)

            a >>= 1
            b >>= 1
            c >>= 1
        return ans


if __name__ == "__main__":
    assert Solution().minFlips(a=2, b=6, c=5) == 3
    assert Solution().minFlips(a=4, b=2, c=7) == 1
    assert Solution().minFlips(a=1, b=2, c=3) == 0
