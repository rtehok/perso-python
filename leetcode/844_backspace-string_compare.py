import itertools


class Solution:
    def backspaceCompareV1(self, s: str, t: str) -> bool:
        stack_1 = []

        i = 0
        while i < len(s):
            if s[i] != "#":
                stack_1.append(s[i])
                i += 1
                continue

            while i < len(s) and s[i] == "#":
                if stack_1:
                    stack_1.pop()
                i += 1

        stack_2 = []
        j = 0
        while j < len(t):
            if t[j] != "#":
                stack_2.append(t[j])
                j += 1
                continue

            while j < len(t) and t[j] == "#":
                if stack_2:
                    stack_2.pop()
                j += 1

        return stack_1 == stack_2

    """O(M + N) / O(M + N)"""
    def backspaceCompareV2(self, s: str, t: str) -> bool:
        stack_1 = []
        stack_2 = []

        for c in s:
            if c == '#' and stack_1:
                stack_1.pop()
            elif c != '#':
                stack_1.append(c)

        for c in t:
            if c == '#' and stack_2:
                stack_2.pop()
            elif c != '#':
                stack_2.append(c)

        return stack_1 == stack_2

    """O(M + N) / O(1)"""
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(ss):
            skip = 0
            for c in reversed(ss):
                if c == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c

        return all(x == y for x, y in itertools.zip_longest(helper(s), helper(t)))


if __name__ == "__main__":
    assert Solution().backspaceCompare("ab#c", "ad#c")
    assert Solution().backspaceCompare("ab##", "c#d#")
    assert not Solution().backspaceCompare("a#c", "b")
    assert Solution().backspaceCompare("a##c", "#a#c")
    assert Solution().backspaceCompare("y#fo##f", "y#f#o##f")
