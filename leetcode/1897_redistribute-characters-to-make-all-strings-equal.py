from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = [0] * 26
        for word in words:
            for c in word:
                cnt[ord(c) - ord('a')] += 1

        n = len(words)

        for v in cnt:
            if v % n != 0:
                return False

        return True


assert Solution().makeEqual(["abc", "aabc", "bc"])
assert not Solution().makeEqual(["ab", "a"])
