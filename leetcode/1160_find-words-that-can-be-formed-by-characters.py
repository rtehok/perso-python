from collections import Counter
from typing import List


class Solution:
    def countCharactersV1(self, words: List[str], chars: str) -> int:
        ans = 0
        chars_cnt = Counter(chars)
        for word in words:
            word_cnt = Counter(word)

            good = True
            for c, freq in word_cnt.items():
                if chars_cnt[c] < freq:
                    good = False
                    break

            if good:
                ans += len(word)

        return ans

    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = [0] * 26
        for c in chars:
            cnt[ord(c) - ord('a')] += 1

        ans = 0
        for word in words:
            word_cnt = [0] * 26

            for c in word:
                word_cnt[ord(c) - ord('a')] += 1

            good = True
            for i in range(26):
                if cnt[i] < word_cnt[i]:
                    good = False
                    break

            if good:
                ans += len(word)

        return ans


if __name__ == "__main__":
    assert Solution().countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach") == 6
    assert Solution().countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr") == 10
