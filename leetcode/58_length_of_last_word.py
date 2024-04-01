class Solution:
    def lengthOfLastWordV1(self, s: str) -> int:
        n = len(s)
        right = n - 1
        while s[right] == " ":
            right -= 1

        if right == 0 and s[right] != 0:
            return 1

        for left in range(right, -1, -1):
            if s[left] == " ":
                return right - left
            if left == 0:
                return right - left + 1

        return right

    def lengthOfLastWord(self, s: str) -> int:
        ans = 0

        for c in s[::-1]:
            if c == " ":
                if ans == 0:
                    continue
                else:
                    break
            else:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
    print(Solution().lengthOfLastWord("luffy is still joyboy"))
