class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = 0

        while numBottles >= numExchange:
            consumed_bottles += numExchange
            numBottles -= numExchange

            numBottles += 1

        return numBottles + consumed_bottles


assert Solution().numWaterBottles(numBottles=15, numExchange=4) == 19
assert Solution().numWaterBottles(numBottles=9, numExchange=3) == 13
