class Solution:
    def myAtoi(self, s: str) -> int:
        state = "start"
        sign = 1
        res = 0
        for c in s:
            if state == "start":
                if c.isspace():
                    continue
                elif c == "-":
                    sign = -1
                    state = "read"
                elif c == "+":
                    sign = 1
                    state = "read"
                elif c.isdigit():
                    res = int(c)
                    state = "read"
                else:
                    break
            elif state == "read":
                if c.isdigit():
                    res = res * 10 + int(c)
                else:
                    break

        return min(int(2 ** 31) - 1, max(-int(2 ** 31), res * sign))


if __name__ == "__main__":
    assert Solution().myAtoi("42") == 42
    assert Solution().myAtoi("4193 with words") == 4193
    assert Solution().myAtoi("0032") == 32
    assert Solution().myAtoi("   -42") == -42
    assert Solution().myAtoi("-91283472332") == -2147483648
    assert Solution().myAtoi("+-12") == 0
    assert Solution().myAtoi("-+12") == 0
    assert Solution().myAtoi("--12") == 0
    assert Solution().myAtoi("00000-42a1234") == 0
