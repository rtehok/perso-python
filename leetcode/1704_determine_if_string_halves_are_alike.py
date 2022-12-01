class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')

        mid = len(s) // 2 - 1 if len(s) % 2 == 0 else len(s) // 2
        i, j = mid, mid + 1
        count = 0

        while i >= 0:
            if s[i] in vowels:
                count += 1
            i -= 1

        while j < len(s):
            if s[j] in vowels:
                count -= 1
            j += 1

        return count == 0


if __name__ == "__main__":
    assert Solution().halvesAreAlike("book")
    assert not Solution().halvesAreAlike("textbook")
