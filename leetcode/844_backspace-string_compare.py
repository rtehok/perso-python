import itertools


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """O(M + N) / O(M + N)"""
        # stack_1 = []
        # stack_2 = []
        #
        # for c in s:
        #     if c == '#' and stack_1:
        #         stack_1.pop()
        #     elif c != '#':
        #         stack_1.append(c)
        #
        # for c in t:
        #     if c == '#' and stack_2:
        #         stack_2.pop()
        #     elif c != '#':
        #         stack_2.append(c)
        #
        # return stack_1 == stack_2
        """O(M + N) / O(1)"""
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
