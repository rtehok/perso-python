from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        # print("".join([c * f for c, f in sorted(Counter(s).items(), key=lambda kv: kv[1], reverse=True)]))
        return "".join([c * f for c, f in Counter(s).most_common()])

    def bucketFrequencySort(self, s: str) -> str:
        c = Counter(s)

        max_freq = max(c.values())

        freq = [[] for _ in range(max_freq + 1)]

        for c, f in c.items():
            freq[f].append(c)

        res = []
        # iterate in freq => O(n)
        for f in reversed(range(max_freq + 1)):
            for c in freq[f]:
                res.append(c * f)

        return "".join(res)


if __name__ == "__main__":
    assert Solution().frequencySort("tree") == "eetr"
    assert Solution().frequencySort("cccaaa") == "cccaaa"
    assert Solution().frequencySort("Aabb") == "bbAa"
    assert Solution().bucketFrequencySort("tree") == "eetr"
    assert Solution().bucketFrequencySort("cccaaa") == "cccaaa"
    assert Solution().bucketFrequencySort("Aabb") == "bbAa"
