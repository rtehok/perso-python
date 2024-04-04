class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                stack.pop()

            ans = max(ans, len(stack))
        return ans


assert Solution().maxDepth(s="(1+(2*3)+((8)/4))+1") == 3
assert Solution().maxDepth(s="(1)+((2))+(((3)))") == 3
