class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        test_per_pig = minutesToTest // minutesToDie + 1

        pigs = 0

        while (test_per_pig ** pigs) < buckets:
            pigs += 1

        return pigs


if __name__ == "__main__":
    assert Solution().poorPigs(buckets=4, minutesToDie=15, minutesToTest=15) == 2
    assert Solution().poorPigs(buckets=4, minutesToDie=15, minutesToTest=30) == 2
