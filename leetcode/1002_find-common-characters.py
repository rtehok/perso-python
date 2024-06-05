import functools
from collections import Counter
from typing import List


class Solution:
    def commonCharsV1(self, words: List[str]) -> List[str]:
        ans = []
        first = words[0]
        words_cnt = [Counter(word) for word in words[1:]]
        for c in first:
            for other in words_cnt:
                if c in other:
                    other[c] -= 1

            if all(c in other and other[c] >= 0 for other in words_cnt):
                ans.append(c)
        return ans

    def commonCharsCounters(self, words: List[str]) -> List[str]:
        common_char_counter = Counter(words[0])

        for word in words[1:]:
            curr_char_counter = Counter(word)

            for c in common_char_counter.keys():
                common_char_counter[c] = min(
                    common_char_counter[c], curr_char_counter[c]
                )

        res = []
        for c, count in common_char_counter.items():
            for _ in range(count):
                res.append(c)

        return res

    def commonChars(self, words: List[str]) -> List[str]:
        return functools.reduce(lambda x, y: x & y, map(Counter, words)).elements()


assert sorted(Solution().commonChars(["cool", "lock", "cook"])) == ["c", "o"]
assert sorted(Solution().commonChars(["bella", "label", "roller"])) == ["e", "l", "l"]
