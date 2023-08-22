class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        while columnNumber > 0:
            columnNumber -= 1
            res = arr[columnNumber % 26] + res
            columnNumber //= 26

        return res


if __name__ == "__main__":
    assert Solution().convertToTitle(1) == "A"
    assert Solution().convertToTitle(28) == "AB"
    assert Solution().convertToTitle(701) == "ZY"
