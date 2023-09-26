class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        for i, char in enumerate(s):
            if char in stack:
                continue

            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                stack.pop()

            stack.append(char)

        return "".join(stack)


if __name__ == "__main__":
    assert Solution().removeDuplicateLetters("cbacdcbc") == "acdb"
    assert Solution().removeDuplicateLetters("bcabc") == "abc"
