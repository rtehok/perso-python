class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        stack = stack[:-k] if k > 0 else stack
        res = "".join(stack).lstrip('0')
        return res if res else '0'


assert Solution().removeKdigits(num="1432219", k=3) == "1219"
assert Solution().removeKdigits(num="10200", k=1) == "200"
assert Solution().removeKdigits(num="10", k=2) == "0"
