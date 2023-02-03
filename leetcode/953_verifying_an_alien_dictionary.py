from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, c in enumerate(order):
            d[c] = i

        n = len(words)

        for i in range(n - 1):
            if d[words[i][0]] < d[words[i + 1][0]]:
                continue

            j = 1
            while j < min(len(words[i]), len(words[i + 1])):
                if d[words[i][j]] > d[words[i + 1][j]]:
                    return False
                j += 1

            if len(words[i]) > len(words[i + 1]) and d[words[i][j - 1]] == d[words[i + 1][j - 1]]:
                return False

        return True


if __name__ == "__main__":
    assert Solution().isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
    assert not Solution().isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")
    assert not Solution().isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz")
    assert Solution().isAlienSorted(words=["apap", "app"], order="abcdefghijklmnopqrstuvwxyz")
