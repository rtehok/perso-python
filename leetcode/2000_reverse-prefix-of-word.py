class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end = 0
        while end < len(word) and word[end] != ch:
            end += 1

        if end == len(word):
            return word

        return word[:end + 1][::-1] + word[end + 1:]


assert Solution().reversePrefix(word="abcdefd", ch="d") == "dcbaefd"
assert Solution().reversePrefix(word="xyxzxe", ch="z") == "zxyxxe"
assert Solution().reversePrefix(word="abcd", ch="z") == "abcd"
