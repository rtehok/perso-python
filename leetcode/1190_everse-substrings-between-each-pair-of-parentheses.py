class Solution:
    def reverseParenthesesV1(self, s: str) -> str:
        open_parentheses_indices = []
        res = []

        for c in s:
            if c == "(":
                open_parentheses_indices.append(len(res))
            elif c == ")":
                start = open_parentheses_indices.pop()
                res[start:] = res[start:][::-1]
            else:
                res.append(c)

        return "".join(res)

    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n

        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i

        res = []
        curr_idx = 0
        dir = 1

        while curr_idx < n:
            if s[curr_idx] in ["(", ")"]:
                curr_idx = pair[curr_idx]
                dir = -dir
            else:
                res.append(s[curr_idx])
            curr_idx += dir

        return "".join(res)


assert Solution().reverseParentheses(s="(abcd)") == "dcba"
assert Solution().reverseParentheses(s="(u(love)i)") == "iloveu"
assert Solution().reverseParentheses(s="(ed(et(oc))el)") == "leetcode"
