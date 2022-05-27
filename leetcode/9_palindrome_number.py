class Solution:
    def isPalindrome(self, x: int) -> bool:
        inverted = 0
        tmp = x

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        while tmp > inverted:
            inverted = inverted * 10 + tmp % 10
            tmp //= 10

        return inverted == tmp or tmp == inverted // 10


if __name__ == "__main__":
    assert Solution().isPalindrome(121)
    assert not Solution().isPalindrome(-121)
    assert not Solution().isPalindrome(10)
