class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        for c in s:
            # if stack and stack[-1] != c and (stack[-1].lower() == c or stack[-1].upper() == c):
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


assert Solution().makeGood("leEeetcode") == "leetcode"
assert Solution().makeGood("abBAcC") == ""
assert Solution().makeGood("s") == "s"