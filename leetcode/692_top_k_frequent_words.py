import collections
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counters = collections.Counter(words)
        arr = sorted([[word, freq] for word, freq in counters.items()], key=lambda x: x[0])  # sort words alphabetically
        arr = sorted(arr, key=lambda x: x[1], reverse=True)  # sort by number

        return [arr[i][0] for i in range(k)]


if __name__ == "__main__":
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
    assert Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == [
        "the", "is", "sunny", "day"]
