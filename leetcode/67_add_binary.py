class Solution:
    def addBinaryV1(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]

    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        i = 0
        carry = 0
        while i < len(a) or i < len(b) or carry != 0:
            x = 0
            if i < len(a) and a[len(a) - 1 - i] == "1":
                x = 1

            y = 0
            if i < len(b) and b[len(b) - 1 - i] == "1":
                y = 1

            ans = str((x + y + carry) % 2) + ans
            carry = (x + y + carry) // 2
            i += 1

        return ans


if __name__ == "__main__":
    assert Solution().addBinary(a="11", b="1") == "100"
    assert Solution().addBinary(a="1010", b="1011") == "10101"
