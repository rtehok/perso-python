class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        a = sorted(d.keys(), reverse=True)
        res = ""
        while num > 0:
            for x in a:
                while num >= x:
                    res += d[x]
                    num -= x

        return res


if __name__ == "__main__":
    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(1994) == "MCMXCIV"
