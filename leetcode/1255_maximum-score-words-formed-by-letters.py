from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        w = len(words)
        freq = [0 for _ in range(26)]
        for c in letters:
            freq[ord(c) - ord('a')] += 1

        def subset_score(subset_letters):
            total_score = 0

            for c in range(26):
                if subset_letters[c] > freq[c]:
                    return 0
                total_score += subset_letters[c] * score[c]

            return total_score

        max_score = 0

        for mask in range(1 << w):
            subset_letters = [0 for _ in range(26)]
            for i, word in enumerate(words):
                if (mask & (1 << i)) > 0:
                    for j in range(len(word)):
                        subset_letters[ord(word[j]) - ord("a")] += 1
            max_score = max(max_score, subset_score(subset_letters))

        return max_score


assert Solution().maxScoreWords(words=["dog", "cat", "dad", "good"],
                                letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                                score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                       0]) == 23
assert Solution().maxScoreWords(words=["xxxz", "ax", "bx", "cx"], letters=["z", "a", "b", "c", "x", "x", "x"],
                                score=[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
                                       10]) == 27
assert Solution().maxScoreWords(words=["leetcode"], letters=["l", "e", "t", "c", "o", "d"],
                                score=[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                                       0]) == 0
