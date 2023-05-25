import math


class Solution:
    # TC O(n * maxPts)
    def new21GameV1(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)  # let dp[i] be the proba of having exactly i points (i <= n)
        dp[0] = 1  # starts with 0 points

        for i in range(1, n + 1):
            for j in range(1, maxPts + 1):  # let j be the number drawn
                # moving from dp[i - j] to dp[i] is done when drawing j
                # Alice stops drawing numbers when she gets k or more points.
                if 0 <= i - j < k:
                    # The probability of drawing j points at the state dp[i−j] is 1 / maxPts
                    # because all numbers in the range [1,maxPts] are equiprobable.
                    # Thus the probability of transitioning from dp[i−j] to dp[i] is 1 / maxPts
                    # To calculate dp[i], we need to consider all possible values of j, and sum all the probabilities.
                    dp[i] += dp[i - j] / maxPts
        # dp[i] for k <= i <= n is the state of the game when it's over, and Alice has n or fewer points.
        # It implies that the answer to the problem is the sum of dp for all such states.
        return sum(dp[k:])

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1

        s = 1 if k > 0 else 0
        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:  # sliding window, move s to the right
                s -= dp[i - maxPts]

        return sum(dp[k:])


if __name__ == "__main__":
    assert math.isclose(Solution().new21Game(n=21, k=17, maxPts=10), 0.73278, rel_tol=10 ** -5)
    assert math.isclose(Solution().new21Game(n=10, k=1, maxPts=10), 1.0, rel_tol=10 ** -5)
    assert math.isclose(Solution().new21Game(n=6, k=1, maxPts=10), 0.6, rel_tol=10 ** -5)
    assert math.isclose(Solution().new21Game(n=9811, k=8776, maxPts=1096), 0.99696, rel_tol=10 ** -5)
