class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        monday = 1

        while n > 0:
            for day in range(min(n, 7)):
                ans += (monday + day)

            n -= 7
            monday += 1

        return ans


if __name__ == "__main__":
    assert Solution().totalMoney(20) == 96
    assert Solution().totalMoney(4) == 10
    assert Solution().totalMoney(10) == 37
