import operator
from math import trunc
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operate = {
            "+": operator.add,
            "-": operator.sub,
            "/": operator.truediv,
            "*": operator.mul,
        }

        for token in tokens:
            if token not in {"+", "-", "/", "*"}:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                stack.append(trunc(operate[token](left, right)))

        return stack[0]


if __name__ == "__main__":
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
