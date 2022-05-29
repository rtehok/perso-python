class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        def helper(s: str) -> str:
            cnt = 1
            res = []
            for i in range(len(s)):
                if i + 1 == len(s) or s[i + 1] != s[i]:
                    res.append(f"{cnt}{s[i]}")
                    cnt = 1
                else:
                    cnt += 1
            return "".join(res)

        return helper(self.countAndSay(n - 1))


if __name__ == "__main__":
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(4) == "1211"
