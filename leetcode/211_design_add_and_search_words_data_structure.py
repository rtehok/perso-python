import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:

    # def __init__(self):
    #     self.children = [None] * 26
    #     self.is_complete_word = False
    #
    # def addWord(self, word: str) -> None:
    #     curr = self  # create a Trie
    #     for c in word:
    #         if not curr.children[ord(c) - ord('a')]:
    #             curr.children[ord(c) - ord('a')] = WordDictionary()
    #         curr = curr.children[ord(c) - ord('a')]  # move to next
    #     curr.is_complete_word = True
    #
    # def search(self, word: str) -> bool:
    #     curr = self
    #     for i, c in enumerate(word):
    #         if c == '.':
    #             for char_node in curr.children:
    #                 if char_node and char_node.search(word[i + 1:]):
    #                     return True
    #             return False
    #
    #         if not curr.children[ord(c) - ord('a')]:
    #             return False
    #
    #         curr = curr.children[ord(c) - ord('a')]
    #
    #     return curr and curr.is_complete_word

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_word

            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True

            if word[index] in node.children:
                return dfs(node.children[word[index]], index + 1)

            return False

        return dfs(self.root, 0)


if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    assert not obj.search("pad")
    assert obj.search("bad")
    assert obj.search(".ad")
    assert obj.search("b..")
