class Solution:
    def reverse(self, x: int) -> int:
        # def loop(is_positive, d, res):
        #     if d < 10:
        #         res = res * 10 + d
        #         if is_positive and (res > 2 ** 31 - 1 or (res // 10 == 2 ** 31 - 1 and d > 7)):
        #             return 0
        #         elif not is_positive and (res > 2 ** 31 or (res // 10 == 2 ** 31 and d > 8)):
        #             return 0
        #         return res if is_positive else -res
        #
        #     return loop(is_positive, d // 10, res * 10 + d % 10)
        #
        # return loop(x > 0, abs(x), 0)
        res = 0
        tmp = abs(x)
        while tmp != 0:
            pop = tmp % 10
            tmp //= 10
            if res >= (2 ** 31) / 10 or (res == 2 ** 31 - 1 and pop > 7) or (res == 2 ** 31 and pop > 8):
                return 0
            res = res * 10 + pop

        return res if x > 0 else -res


if __name__ == "__main__":
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
    assert Solution().reverse(1534236469) == 0
