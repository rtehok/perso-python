import collections
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_t = collections.Counter(t)
        required = len(dict_t)

        l, r = 0, 0

        formed = 0

        window_count = collections.defaultdict(int)

        ans = math.inf, None, None  # window length, left, right

        while r < len(s):
            char = s[r]
            window_count[char] += 1

            if char in dict_t and window_count[char] == dict_t[char]:
                formed += 1

            while l <= r and formed == required:
                char = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_count[char] -= 1
                if char in dict_t and window_count[char] < dict_t[char]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == math.inf else s[ans[1]: ans[2] + 1]


if __name__ == "__main__":
    assert Solution().minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert Solution().minWindow(s="a", t="a") == "a"
    assert Solution().minWindow(s="a", t="aa") == ""
