import collections
from functools import reduce
from typing import List


class Solution:
    # def minimumLengthEncoding(self, words: List[str]) -> int:
    #     good = set(words)
    #     for word in words:
    #         for k in range(1, len(word)):
    #             good.discard(word[k:])
    #
    #     return sum([len(word) + 1 for word in good])

    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        # reverse the word, look for same suffix, reduce result is trie minus suffix (if found) and added to trie if not found
        # 0: "time": trie = { e: { m: { i: { t: {} } } } } --> result = {}
        # 1: "me": trie = { e: { m: { i: { t: {} } } } } --> result = { i: { t: {} } }
        # 2: "bell": trie = { e: { m: { i: { t: {} } } }, l: { l: { e: { b: {} } } } --> result = {}

        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
        # nodes = [reduce(lambda d, k: d[k], word[::-1], trie) for word in words]

        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)


if __name__ == "__main__":
    assert Solution().minimumLengthEncoding(["time", "me", "bell"]) == 10
