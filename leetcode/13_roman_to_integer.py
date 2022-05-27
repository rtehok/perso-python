class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        i = 0
        while i <= len(s) - 1:
            c = s[i]
            if i + 1 <= len(s) - 1 and d[c] < d[s[i + 1]]:
                res += d[s[i + 1]] - d[c]
                i += 2
                continue

            if c in d:
                res += d[c]
                i += 1

        return res


if __name__ == "__main__":
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994
