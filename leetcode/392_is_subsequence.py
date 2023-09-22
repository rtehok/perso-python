class Solution:
    def isSubsequenceV1(self, s: str, t: str) -> bool:
        # if len(s) > len(t):
        #     return False
        #
        # def helper(ss, tt):
        #     if not len(ss):
        #         return True
        #
        #     if not len(tt):
        #         return False
        #
        #     if ss[0] == tt[0]:
        #         return helper(ss[1:], tt[1:])
        #     else:
        #         return helper(ss, tt[1:])
        #
        # return helper(s, t)
        if len(s) > len(t):
            return False

        subsequence_length = 0

        for i in range(len(t)):
            if subsequence_length <= len(s) - 1:
                if s[subsequence_length] == t[i]:
                    subsequence_length += 1

        return subsequence_length == len(s)

    def isSubsequenceV2(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return False

        p1 = p2 = 0

        while p1 < m:
            if p2 == n:
                return False

            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            elif p2 < n:
                p2 += 1

        return True

    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1

            j += 1

        return i == len(s)


if __name__ == "__main__":
    assert Solution().isSubsequence("abc", "ahbgdc")
    assert not Solution().isSubsequence("axc", "ahbgdc")
    assert Solution().isSubsequence("b", "abc")
