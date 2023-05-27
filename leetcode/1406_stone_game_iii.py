from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i] represents the maximum score difference Alice can achieve starting from the i-th stone

        for i in range(n - 1, -1, -1):
            max_score = float('-inf')
            total_score = 0

            for j in range(i, min(i + 3, n)):
                total_score += stoneValue[j]
                max_score = max(max_score, total_score - dp[j + 1])

            dp[i] = max_score

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"


if __name__ == "__main__":
    assert Solution().stoneGameIII([1, 2, 3, 7]) == "Bob"
    assert Solution().stoneGameIII([1, 2, 3, -9]) == "Alice"
    assert Solution().stoneGameIII([1, 2, 3, 6]) == "Tie"
