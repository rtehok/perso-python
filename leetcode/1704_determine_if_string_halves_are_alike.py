class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        mid = n // 2
        n1, n2 = 0, 0
        vowels = set("aeiouAEIOU")
        for i in range(mid):
            if s[i] in vowels:
                n1 += 1
        for i in range(mid, n):
            if s[i] in vowels:
                n2 += 1

        return n1 == n2


if __name__ == "__main__":
    assert Solution().halvesAreAlike("book")
    assert not Solution().halvesAreAlike("textbook")
