class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        s = " " + s + " "
        end = -1

        for i in range(len(s) - 2, 0, -1):
            if s[i] != " ":  # if current is not a space char
                if s[i + 1] == " ":  # if right char is a space char, set end variable
                    end = i
                if s[i - 1] == " ":  # if left char is a space char
                    start = i  # set start to current index
                    res = res + " " + s[start: end + 1]  # add to res the word (start to end)

        return res[1:]  # remove first char that is a space


if __name__ == "__main__":
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"
    assert Solution().reverseWords("  hello world  ") == "world hello"
    assert Solution().reverseWords("a good   example") == "example good a"
