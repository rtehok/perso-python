class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = [[-1] * 101 for _ in range(101)]
        n = len(s)

        def solve(i, K):
            k = K
            if n - i <= k:
                return 0
            if memo[i][K] != -1:
                return memo[i][K]

            ans = solve(i + 1, k - 1) if k > 0 else 101
            c = 1
            for j in range(i + 1, n + 1):
                ans = min(ans, 1 + (3 if (c > 99) else 2 if (c > 9) else 1 if (c > 1) else 0) + solve(j, k))
                if j < n and s[i] == s[j]:
                    c += 1
                else:
                    k -= 1
                    if k < 0:
                        break
            memo[i][K] = ans

            return ans

        return solve(0, k)


assert Solution().getLengthOfOptimalCompression(s="aaabcccd", k=2) == 4
assert Solution().getLengthOfOptimalCompression(s="aabbaa", k=2) == 2
assert Solution().getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0) == 3
