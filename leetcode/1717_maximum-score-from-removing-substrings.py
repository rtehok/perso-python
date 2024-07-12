class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pair = [("ab", x), ("ba", y)]
        if x < y:
            pair[0], pair[1] = pair[1], pair[0]

        res = 0
        for (c1, c2), p in pair:
            stack = []
            for c in s:
                if stack and stack[-1] == c1 and c == c2:
                    stack.pop()
                    res += p
                else:
                    stack.append(c)
            s = stack
        return res


assert Solution().maximumGain(s="cdbcbbaaabab", x=4, y=5) == 19
assert Solution().maximumGain(s="aabbaaxybbaabb", x=5, y=4) == 20
