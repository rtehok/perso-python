class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        s1map = [0] * 26
        s2map = [0] * 26
        if n1 > n2:
            return False

        for i in range(n1):
            s1map[ord(s1[i]) - ord('a')] += 1

        for i in range(n2):
            s2map[ord(s2[i]) - ord('a')] += 1
            if i >= n1:
                s2map[ord(s2[i - n1]) - ord('a')] -= 1  # sliding window

            if s1map == s2map:
                return True

        return False


if __name__ == "__main__":
    assert Solution().checkInclusion(s1="ab", s2="eidbaooo")
    assert not Solution().checkInclusion(s1="ab", s2="eidboaoo")
    assert Solution().checkInclusion("adc", "dcda")
    assert not Solution().checkInclusion("hello", "ooolleoooleh")
