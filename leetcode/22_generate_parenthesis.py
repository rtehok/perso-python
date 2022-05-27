from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(tmp, left, right):
            if len(tmp) == 2 * n:
                res.append(tmp)
                return

            if left < n:
                helper(f"{tmp}(", left + 1, right)

            if right < left:
                helper(f"{tmp})", left, right + 1)

        helper("", 0, 0)

        return res


if __name__ == "__main__":
    assert Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert Solution().generateParenthesis(1) == ["()"]
