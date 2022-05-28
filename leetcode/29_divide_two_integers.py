class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0

        while dividend >= divisor:
            tmp, cnt = divisor, 1
            # print(f"tmp {tmp}, cnt {cnt}")
            while dividend >= tmp:
                # print(f"before dividend {dividend}, tmp {tmp}, res {res}, cnt {cnt}")
                dividend -= tmp
                res += cnt
                cnt += cnt
                tmp += tmp
                # print(f"after dividend {dividend}, tmp {tmp}, res {res}, cnt {cnt}")
        if not positive:
            res = -res

        return min(max(-2 ** 31, res), 2 ** 31 - 1)


if __name__ == "__main__":
    assert Solution().divide(20, 5) == 4
    assert Solution().divide(10, 3) == 3
    assert Solution().divide(7, -3) == -2
