class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        count = 1

        for i in range(2, n + 1):
            count = (count * (2 * i - 1) * i) % MOD

        return count


if __name__ == "__main__":
    assert Solution().countOrders(1) == 1
    assert Solution().countOrders(2) == 6
    assert Solution().countOrders(3) == 90
