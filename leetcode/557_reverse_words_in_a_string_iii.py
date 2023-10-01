class Solution:
    def reverseWordsV0(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split(" ")])

    def reverseWordsV1(self, s: str) -> str:
        res = ""

        n = len(s)
        last_space_index = -1
        for i in range(n):
            if i == n - 1 or s[i] == " ":
                reverse_str_index = i if i == n - 1 else i - 1
                for j in range(reverse_str_index, last_space_index, -1):
                    res += s[j]

                if i != n - 1:
                    res += " "

                last_space_index = i

        return res

    def reverseWords(self, s: str) -> str:
        n = len(s)
        last_space_index = -1

        s = [x for x in s]

        for i in range(n + 1):
            if i == n or s[i] == " ":
                start = last_space_index + 1
                end = i - 1
                while start < end:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                last_space_index = i

        return "".join(s)


if __name__ == "__main__":
    assert Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert Solution().reverseWords("God Ding") == "doG gniD"
    assert Solution().reverseWords("I love u") == "I evol u"
