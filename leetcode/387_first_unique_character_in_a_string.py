from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)

        for k, v in d.items():
            if len(v) == 1:
                return v[0]

        return -1


if __name__ == "__main__":
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
    assert Solution().firstUniqChar("aabb") == -1
