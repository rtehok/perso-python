class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0

        for c in s[::-1]:
            if c == " ":
                if res == 0:
                    continue
                else:
                    break
            else:
                res += 1

        return res


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
    print(Solution().lengthOfLastWord("luffy is still joyboy"))
