from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1
        while left <= right:
            mid = right - (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if left == n:
            return letters[0]

        return letters[left]


if __name__ == "__main__":
    assert Solution().nextGreatestLetter(letters=["c", "f", "j"], target="a") == "c"
    assert Solution().nextGreatestLetter(letters=["c", "f", "j"], target="c") == "f"
    assert Solution().nextGreatestLetter(letters=["x", "x", "y", "y"], target="z") == "x"
