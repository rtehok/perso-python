from typing import List


class Solution:
    def stoneGameV1(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[[None] * n for _ in range(n)] for _ in (0, 1)]

        def helper(alice, first, last):
            if first > last:
                return 0, 0

            if dp[alice][first][last]:
                return dp[alice][first][last]

            alice_score, bob_score = 0, 0
            if alice:
                next_player = not alice
                alice_score = max(alice_score,
                                  piles[first] + helper(next_player, first + 1, last)[0],
                                  piles[last] + helper(next_player, first, last - 1)[0])
            else:
                next_player = alice
                bob_score = max(bob_score,
                                piles[first] + helper(next_player, first + 1, last)[1],
                                piles[last] + helper(next_player, first, last - 1)[1])

            dp[alice][first][last] = alice_score, bob_score
            return alice_score, bob_score

        alice_score, bob_score = helper(True, 0, n - 1)

        return alice_score > bob_score

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[[None] * n for _ in range(n)] for _ in (0, 1)]

        def helper(i, j):
            if i > j:
                return 0

            alice = (j - i - n) % 2

            if dp[alice][i][j]:
                return dp[alice][i][j]

            if alice == 1:
                alice_score = max(piles[i] + helper(i + 1, j), piles[j] + helper(i, j - 1))
            else:
                # bob is playing, trying to minimize alice's score and deducting the pile[i] from alice's score
                alice_score = min(-piles[i] + helper(i + 1, j), -piles[j] + helper(i, j - 1))

            dp[alice][i][j] = alice_score
            return alice_score

        return helper(0, n - 1) > 0


if __name__ == "__main__":
    assert Solution().stoneGame([5, 3, 4, 5])
    assert Solution().stoneGame([3, 7, 2, 3])
