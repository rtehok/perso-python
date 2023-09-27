class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        i = 0

        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1

        for j in range(i - 1, -1, -1):
            char = s[j]
            if char.isdigit():
                length //= int(char)
                k %= length
            else:
                if k == 0 or k == length:
                    return char
                length -= 1


if __name__ == "__main__":
    assert Solution().decodeAtIndex(s="leet2code3", k=10) == "o"
    assert Solution().decodeAtIndex(s="ha22", k=5) == "h"
    assert Solution().decodeAtIndex(s="a2345678999999999999999", k=1) == "a"
