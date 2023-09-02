import collections
import functools
from typing import List


class Solution:
    def minExtraCharTopDown(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        n = len(s)

        @functools.cache
        def dfs(start):
            if start == n:
                return 0

            ans = dfs(start + 1) + 1
            for end in range(start, n):
                curr = s[start:end + 1]
                if curr in dictionary:
                    ans = min(ans, dfs(end + 1))
            return ans

        return dfs(0)

    def minExtraCharBottomUp(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary = set(dictionary)
        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start:end + 1]
                if curr in dictionary:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]

    def minExtraCharDFSWithTrie(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary = set(dictionary)

        root = TrieNode()

        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isWord = True

        @functools.cache
        def dfs(start):
            if start == n:
                return 0

            ans = dfs(start + 1) + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break

                node = node.children[s[end]]
                if node.isWord:
                    ans = min(ans, dfs(end + 1))
            return ans

        return dfs(0)

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary = set(dictionary)
        dp = [0] * (n + 1)

        root = TrieNode()

        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isWord = True

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break

                node = node.children[s[end]]
                if node.isWord:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


if __name__ == "__main__":
    assert Solution().minExtraChar(s="LTSCD", dictionary=["LT", "CD"]) == 1
    assert Solution().minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"]) == 1
    assert Solution().minExtraChar(s="sayhelloworld", dictionary=["hello", "world"]) == 3
