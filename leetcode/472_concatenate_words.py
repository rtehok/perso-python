from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []

        h = set(words)

        for word in words:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(n):
                if not dp[i]:
                    continue
                for j in range(i + 1, n + 1):
                    if j - i < n and word[i:j] in h:
                        dp[j] = True
                if dp[n]:
                    res.append(word)
                    break

        return res


if __name__ == "__main__":
    assert Solution().findAllConcatenatedWordsInADict(
        ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]) == ["catsdogcats",
                                                                                                          "dogcatsdog",
                                                                                                          "ratcatdogcat"]
    assert Solution().findAllConcatenatedWordsInADict(["cat", "dog", "catdog"]) == ["catdog"]
