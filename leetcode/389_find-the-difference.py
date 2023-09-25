import collections


class Solution:
    def findTheDifferenceSorted(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]

        return t[-1]

    def findTheDifferenceBit(self, s: str, t: str) -> str:
        result = 0

        for x in s:
            result ^= ord(x)

        for y in t:
            result ^= ord(y)

        return chr(result)

    def findTheDifference(self, s: str, t: str) -> str:
        cnt_x = collections.Counter(s)
        cnt_y = collections.Counter(t)

        for k, v in cnt_y.items():
            if cnt_x[k] < v:
                return k

        return ""


if __name__ == "__main__":
    assert Solution().findTheDifference(s="abcd", t="abcde") == "e"
    assert Solution().findTheDifference(s="", t="y") == "y"
