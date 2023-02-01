from math import gcd


class Solution:
    # TC O(min(m,n)⋅(m+n))
    # SC O(min(m,n))
    def gcdOfStringsV1(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        def valid(k):
            if l1 % k or l2 % k:
                return False
            n1, n2 = l1 // k, l2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(l1, l2), 0, -1):
            if valid(i):
                return str1[:i]

        return ""

    # TC O(m+n)
    # SC O(m+n)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        max_len = gcd(len(str1), len(str2))
        return str1[:max_len]


if __name__ == "__main__":
    assert Solution().gcdOfStrings(str1="ABCABC", str2="ABC") == "ABC"
    assert Solution().gcdOfStrings(str1="ABABAB", str2="ABAB") == "AB"
