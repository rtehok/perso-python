from typing import List


class Solution:
    def replaceWordsV1(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")

        dictionary.sort()

        for i, word in enumerate(sentence):
            for root in dictionary:
                if word.startswith(root):
                    sentence[i] = root
                    break

        return " ".join(sentence)

    def replaceWordsHash(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary)

        def shortest_root(word):
            for i in range(len(word)):
                root = word[:i]
                if root in d:
                    return root
            return word

        sentence = sentence.split(" ")
        for word in range(len(sentence)):
            sentence[word] = shortest_root(sentence[word])

        return " ".join(sentence)

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        d_trie = Trie()
        for word in dictionary:
            d_trie.insert(word)

        for i in range(len(sentence)):
            sentence[i] = d_trie.shortest_root(sentence[i])

        return " ".join(sentence)


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord('a')] is None:
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.isEnd = True

    def shortest_root(self, word):
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c) - ord('a')] is None:
                return word
            curr = curr.children[ord(c) - ord('a')]
            if curr.isEnd:
                return word[:i + 1]
        return word


assert Solution().replaceWords(dictionary=["cat", "bat", "rat"],
                               sentence="the cattle was rattled by the battery") == "the cat was rat by the bat"
assert Solution().replaceWords(dictionary=["a", "b", "c"], sentence="aadsfasf absbs bbab cadsfafs") == "a a b c"
