class Solution:
    def isPalindrome(self, x: int) -> bool:
        inverted = 0
        tmp = x
        while tmp > 0:
            inverted = inverted * 10 + tmp % 10
            tmp //= 10

        return inverted == x


if __name__ == "__main__":
    assert Solution().isPalindrome(121)
    assert not Solution().isPalindrome(-121)
    assert not Solution().isPalindrome(10)
