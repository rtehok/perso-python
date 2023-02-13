class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (high % 2 != 0 or low % 2 != 0)


if __name__ == "__main__":
    assert Solution().countOdds(low=3, high=7) == 3
    assert Solution().countOdds(low=8, high=10) == 1
    assert Solution().countOdds(low=8, high=11) == 2
    assert Solution().countOdds(low=8, high=12) == 2
    assert Solution().countOdds(low=8, high=13) == 3
    assert Solution().countOdds(low=798273637, high=970699661) == 86213013
    assert Solution().countOdds(low=21, high=22) == 1
