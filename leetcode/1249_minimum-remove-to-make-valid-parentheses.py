class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        res = []
        for i, c in enumerate(s):
            if stack and i == stack[0]:
                stack.pop(0)
                continue
            res.append(c)

        return "".join(res)


assert Solution().minRemoveToMakeValid("))((") == ""
assert Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
assert Solution().minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
