class Solution:
    def isValidV1(self, s: str) -> bool:
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        stack = []
        while s:
            if s[0] in mapping.keys():
                stack.append(s[0])
                s = s[1:]
            else:
                if len(stack) and s[0] == mapping[stack[-1]]:
                    s = s[1:]
                    stack.pop(-1)
                else:
                    return False

        return len(stack) == 0

    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
            elif stack and ((c == ')' and stack[-1] == '(') or
                            (c == ']' and stack[-1] == '[') or
                            (c == '}' and stack[-1] == '{')):
                stack.pop()
            else:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    assert Solution().isValid("()")
    assert Solution().isValid("()[]{}")
    assert not Solution().isValid("(]")
    assert not Solution().isValid("]")
