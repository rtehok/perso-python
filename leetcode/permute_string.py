class Solution:
    def permute(self, string):
        def loop(s, res):
            if len(s) == 0:
                print(res)

            for i in range(len(s)):
                c = s[i]
                loop(s[:i] + s[i + 1:], res + [c])

        loop(string, [])


if __name__ == "__main__":
    Solution().permute("abc")
