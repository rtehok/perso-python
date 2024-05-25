from typing import List


class Solution:
    def wordBreakBackTrack(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        res = []

        n = len(s)

        def backtrack(start, curr):
            if start == n:
                res.append(" ".join(curr))
                return

            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word in word_set:
                    curr.append(word)
                    backtrack(end, curr)
                    curr.pop()

        backtrack(0, [])

        return res

    def wordBreakDFS(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]

            if not remaining:
                return [""]

            res = []
            for i in range(1, len(remaining) + 1):
                curr_word = remaining[:i]
                if curr_word in word_set:
                    for next_word in dfs(remaining[i:]):
                        res.append(curr_word + (" " if next_word else "") + next_word)

            memo[remaining] = res
            return res

        return dfs(s)

    def wordBreakTabulation(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}
        n = len(s)
        word_set = set(wordDict)

        for start in range(n - 1, -1, -1):
            valid_sentences = []
            for end in range(start, n):
                curr_word = s[start: end + 1]
                if curr_word in word_set:
                    if end == n - 1:
                        valid_sentences.append(curr_word)
                    else:
                        sentences_from_next_index = dp.get(end + 1, [])
                        for sentence in sentences_from_next_index:
                            valid_sentences.append(curr_word + " " + sentence)
            dp[start] = valid_sentences

        return dp.get(0, [])

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = {}
        n = len(s)
        for start in range(n, -1, -1):
            valid_sentences = []
            current_node = trie.root

            for end in range(start, n):
                char = s[end]
                idx = ord(char) - ord("a")
                if not current_node.children[idx]:
                    break

                current_node = current_node.children[idx]

                if current_node.isEnd:
                    curr_word = s[start: end + 1]
                    if end == n - 1:
                        valid_sentences.append(curr_word)
                    else:
                        sentences_from_next_index = dp.get(end + 1, [])
                        for sentence in sentences_from_next_index:
                            valid_sentences.append(curr_word + " " + sentence)

            dp[start] = valid_sentences

        return dp.get(0, [])


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isEnd = True


assert set(Solution().wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"])) == {"cats and dog",
                                                                                                     "cat sand dog"}
assert set(Solution().wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"])) == {
    "pine apple pen apple", "pineapple pen apple", "pine applepen apple"}
assert Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]) == []
