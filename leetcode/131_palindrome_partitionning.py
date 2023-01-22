from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # def isPalindrome(start, end):
        #     while start < end:
        #         if s[start] != s[end]:
        #             return False
        #         start += 1
        #         end -= 1
        #     return True

        def backtrack(start, current_list):
            if start >= n:
                res.append(current_list.copy())

            for end in range(start, n):
                # if isPalindrome(start, end):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    current_list.append(s[start:end + 1])
                    backtrack(end + 1, current_list)
                    current_list.pop()

        backtrack(0, [])
        return res


if __name__ == "__main__":
    assert Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert Solution().partition("a") == [["a"]]
