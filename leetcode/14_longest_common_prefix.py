from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for word in strs[1:]:
            min_len = min(len(word), len(longest))
            while True:
                if word[:min_len] == longest[:min_len]:
                    break
                else:
                    min_len -= 1

            longest = longest[:min_len]

        return longest


if __name__ == "__main__":
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
