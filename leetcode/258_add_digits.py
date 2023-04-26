class Solution:
    def addDigitsBruteForce(self, num: int) -> int:
        if num == 0:
            return 0

        while num >= 10:
            num_str = str(num)
            num = 0
            for c in num_str:
                num += int(c)

        return num

    def addDigits(self, num: int) -> int:
        digital_root = 0

        while num > 0:
            digital_root += num % 10
            num = num // 10

            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0

        return digital_root


if __name__ == "__main__":
    assert Solution().addDigits(38) == 2
    assert Solution().addDigits(0) == 0
