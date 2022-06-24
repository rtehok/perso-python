from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    a = ["h", "e", "l", "l", "o"]
    Solution().reverseString(a)
    assert a == ["o", "l", "l", "e", "h"]

    a = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(a)
    assert a == ["h", "a", "n", "n", "a", "H"]
