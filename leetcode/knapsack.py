from typing import List


def solve(weights: List[int], values: List[int], capacity: int) -> int:
    def ks_brute_force(current_weight, n):
        if current_weight == 0 or n == 0:
            return 0

        if weights[n - 1] > current_weight:
            return ks_brute_force(current_weight, n - 1)
        else:
            return max(values[n - 1] + ks_brute_force(current_weight - weights[n - 1], n - 1),
                       ks_brute_force(current_weight, n - 1))

    # return ks_brute_force(capacity, len(weights))

    def ks_dp_bottom_up():
        dp = [[0] * (capacity + 1) for _ in range(len(values) + 1)]

        for i in range(len(values) + 1):
            for w in range(capacity + 1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif weights[i - 1] > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

        # print(dp)

        return dp[-1][-1]

    # return ks_dp_bottom_up()

    def ks_dp_optimized():
        dp = [0] * (capacity + 1)

        for i in range(1, len(values) + 1):
            for w in range(capacity, 0, -1):
                if weights[i - 1] <= w:
                    dp[w] = max(dp[w], dp[w - weights[i - 1]] + values[i - 1])

                print(dp)

        return dp[capacity]

    return ks_dp_optimized()


if __name__ == "__main__":
    print(solve([1, 1, 1], [20, 10, 30], 2))
    print(solve([10, 20, 30], [60, 100, 120], 50))
