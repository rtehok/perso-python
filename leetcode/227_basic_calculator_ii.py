import math


class Solution:
    def calculateStack(self, s: str) -> int:
        if s == "":
            return 0

        n = len(s)

        stack = []

        op = '+'

        current = 0

        for i in range(n):
            c = s[i]

            if str.isdigit(c):
                current = current * 10 + ord(c) - ord('0')

            if not str.isdigit(c) and c != ' ' or i == n - 1:
                if op == '+':
                    stack.append(current)
                elif op == '-':
                    stack.append(-current)
                elif op == '*':
                    stack.append(stack.pop() * current)
                elif op == '/':
                    stack.append(int(stack.pop() / current))

                op = c
                current = 0

        return sum(stack)

    def calculate(self, s: str) -> int:
        if s == "":
            return 0

        n = len(s)

        current, last_number, res = 0, 0, 0

        op = '+'

        for i in range(n):
            c = s[i]
            if str.isdigit(c):
                current = current * 10 + (ord(c) - ord('0'))

            if not str.isdigit(c) and c != ' ' or i == n - 1:
                if op == '+':
                    res += last_number
                    last_number = current
                elif op == '-':
                    res += last_number
                    last_number = -current
                elif op == '*':
                    last_number = last_number * current
                elif op == '/':
                    last_number = int(last_number / current)

                op = c
                current = 0

        res += last_number

        return res


if __name__ == "__main__":
    assert Solution().calculate("14-3/2") == 13
    assert Solution().calculate("3+2*2") == 7
    assert Solution().calculate(" 3/2 ") == 1
    assert Solution().calculate(" 3+5 / 2 ") == 5
