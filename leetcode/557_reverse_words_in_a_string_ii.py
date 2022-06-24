class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(map(lambda l: l[::-1], s.split(" ")))
        i, j = 0, 1
        res = []
        while j < len(s) and i < len(s) - 1:
            if s[j] == " ":
                res.append("".join(s[i:j][::-1]))
                i = j + 1

            j += 1

            if j == len(s) - 1:
                res.append("".join(s[i:j + 1][::-1]))

        return " ".join(res)


if __name__ == "__main__":
    assert Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert Solution().reverseWords("God Ding") == "doG gniD"
    assert Solution().reverseWords("I love u") == "I evol u"
