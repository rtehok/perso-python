import collections


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # s = s.split(" ")
        # pattern = list(pattern)
        # d = {}
        # d2 = {}
        #
        # if len(s) != len(pattern):
        #     return False
        #
        # for i, x in enumerate(s):
        #     if x in d:
        #         s[i] = d[x]
        #     else:
        #         d[x] = i
        #         s[i] = i
        #
        #     if pattern[i] in d2:
        #         pattern[i] = d2[pattern[i]]
        #     else:
        #         d2[pattern[i]] = i
        #         pattern[i] = i
        #
        # return pattern == s
        s = s.split()
        c1 = collections.Counter(pattern)
        c2 = collections.Counter(s)
        c3 = collections.Counter(zip(pattern, s))
        return len(c1) == len(c2) == len(c3) and len(pattern) == len(s)


if __name__ == "__main__":
    assert Solution().wordPattern(pattern="abba", s="dog cat cat dog")
    assert not Solution().wordPattern(pattern="abba", s="dog cat cat fish")
    assert not Solution().wordPattern(pattern="aaaa", s="dog cat cat dog")
    assert not Solution().wordPattern(pattern="aba", s="cat cat cat dog")
