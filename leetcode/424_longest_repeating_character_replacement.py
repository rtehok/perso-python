class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        most_frequent = 0
        left = 0
        output = 0
        for right in range(len(s)):
            seen[s[right]] = 1 + seen.get(s[right], 0)
            most_frequent = max(most_frequent, seen[s[right]])
            while (right - left + 1) - most_frequent > k:  # check that substring is valid
                seen[s[left]] -= 1
                left += 1

            output = max(output, right - left + 1)

        return output


if __name__ == "__main__":
    assert Solution().characterReplacement(s="ABAB", k=2) == 4
    assert Solution().characterReplacement(s="AABABBA", k=1) == 4
