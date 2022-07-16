from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []

        left = 0

        for right in range(len(p), len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            sCount[s[left]] -= 1

            if sCount[s[left]] == 0:
                sCount.pop(s[left])

            left += 1

            if sCount == pCount:
                res.append(left)

        return res


if __name__ == "__main__":
    assert Solution().findAnagrams(s="cbaebabacd", p="abc") == [0, 6]
    assert Solution().findAnagrams(s="abab", p="ab") == [0, 1, 2]
    assert Solution().findAnagrams(s="baa", p="aa") == [1]
    assert Solution().findAnagrams("ababababab", "aab") == [0, 2, 4, 6]
