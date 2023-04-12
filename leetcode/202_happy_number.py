class Solution:
    def isHappyV1(self, n: int) -> bool:
        memo = set()
        while n > 1:
            n_str = str(n)
            if n_str not in memo and (n >= 10 or n % 2 != 0):
                memo.add(n_str)
                n = sum([int(c) ** 2 for c in n_str])
            else:
                return False

        return n == 1

    def isHappy(self, n: int) -> bool:
        seen = set()
        def get_next(n):
            total = 0
            while n > 0:
                n, mod = divmod(n, 10)
                seen.add(n)
                total += mod ** 2
            return total

        while n > 1 and n not in seen:
            n = get_next(n)

        return n == 1


if __name__ == "__main__":
    assert Solution().isHappy(19)
    assert not Solution().isHappy(2)
    assert Solution().isHappy(7)
