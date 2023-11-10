from collections import Counter


class Solution:
    def sortVowelsV1(self, s: str) -> str:
        VOWELS = {"a", "e", "i", "o", "u"}
        tmp = []
        res = [""] * len(s)
        for i, c in enumerate(s):
            if c.lower() in VOWELS:
                tmp.append(c)
            else:
                res[i] = c

        tmp.sort(key=lambda x: ord(x), reverse=True)

        for i, c in enumerate(res):
            if c == "":
                res[i] = tmp.pop()

        return "".join(res)

    def sortVowels(self, s: str) -> str:
        freq = Counter(s)
        res = []

        vowels = list("uoieaUOIEA")
        vowels_set = set(vowels)

        for c in s:
            if c in vowels_set:
                while freq[vowels[-1]] == 0:
                    vowels.pop()
                res.append(vowels[-1])
                freq[vowels[-1]] -= 1
            else:
                res.append(c)

        return "".join(res)


if __name__ == "__main__":
    assert Solution().sortVowels("lEetcOde") == "lEOtcede"
    assert Solution().sortVowels("lYmpH") == "lYmpH"
