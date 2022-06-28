class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = [0] * 26
        for c in s:
            frequency[ord(c) - ord('a')] += 1
        frequency.sort(reverse=True)

        delete_count = 0
        max_freq_allowed = len(s)
        for freq in frequency:
            if freq > max_freq_allowed:
                delete_count += freq - max_freq_allowed
                freq = max_freq_allowed

            max_freq_allowed = max(0, freq - 1)

        return delete_count


if __name__ == "__main__":
    assert Solution().minDeletions("aab") == 0
    assert Solution().minDeletions("aaabbbcc") == 2
    assert Solution().minDeletions("ceabaacb") == 2
