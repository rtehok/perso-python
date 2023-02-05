import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p, len_s = len(p), len(s)
        if len_p > len_s:
            return []

        p_cnt, s_cnt = collections.defaultdict(int), collections.defaultdict(int)

        for i, c in enumerate(p):
            p_cnt[c] += 1
            s_cnt[s[i]] += 1

        res = [0] if p_cnt == s_cnt else []

        left = 0

        for right in range(len_p, len_s):
            s_cnt[s[right]] += 1
            s_cnt[s[left]] -= 1

            if s_cnt[s[left]] <= 0:
                s_cnt.pop(s[left])

            left += 1

            if p_cnt == s_cnt:
                res.append(left)

        return res


if __name__ == "__main__":
    assert Solution().findAnagrams(s="cbaebabacd", p="abc") == [0, 6]
    assert Solution().findAnagrams(s="abab", p="ab") == [0, 1, 2]
    assert Solution().findAnagrams(s="baa", p="aa") == [1]
    assert Solution().findAnagrams("ababababab", "aab") == [0, 2, 4, 6]
