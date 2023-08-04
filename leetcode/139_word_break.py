import collections
from typing import List


class Solution:
    def wordBreakBFS(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        q = collections.deque([0])
        seen = set()

        while q:
            start = q.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    q.append(end)
                    seen.add(end)

        return False

    def wordBreakTopDown(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            if i < 0:
                return True

            for word in wordDict:
                if s[i - len(word) + 1: i + 1] == word and dfs(i - len(word)):
                    dp[i] = True
                    return dp[i]

            dp[i] = False
            return dp[i]

        return dfs(len(s) - 1)

    def wordBreakBottomUp(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n

        for i in range(n):
            for word in wordDict:
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1: i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]

    def wordBreakTrie(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]

            curr.is_word = True

        n = len(s)
        dp = [False] * n
        for i in range(n):
            if i == 0 or dp[i - 1]:
                curr = root
                for j in range(i, n):
                    c = s[j]
                    if c not in curr.children:
                        break

                    curr = curr.children[c]

                    if curr.is_word:
                        dp[j] = True

        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


if __name__ == "__main__":
    assert not Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
    assert Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"])
    assert Solution().wordBreak(s="leetcode", wordDict=["leet", "code"])
