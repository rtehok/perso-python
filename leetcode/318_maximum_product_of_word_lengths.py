from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # maxi = 0
        #
        # char_set = [set(word) for word in words]
        # # print(char_set)
        #
        # for i in range(len(words)):
        #     for j in range(i + 1, len(words)):
        #         if not (char_set[i] & char_set[j]):
        #             maxi = max(maxi, len(words[i]) * len(words[j]))
        #
        # return maxi
        maxi = 0

        n = len(words)
        bit_masks = [0] * n
        lengths = [0] * n

        for i, word in enumerate(words):
            for c in word:
                # print(word, c, ord(c) - ord('a'), 1 << ord(c) - ord('a'))
                bit_masks[i] |= 1 << (ord(c) - ord('a'))
                # print(bit_masks)
            lengths[i] = len(word)

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (bit_masks[i] & bit_masks[j]):
                    maxi = max(maxi, lengths[i] * lengths[j])

        return maxi


if __name__ == "__main__":
    assert Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
    assert Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
    assert Solution().maxProduct(["a", "aa", "aaa", "aaaa"]) == 0
