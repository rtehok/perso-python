from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)

        min_sum = sub_array_sum = sum(cardPoints[:n - k])  # sliding window

        for i in range(n - k, n):
            sub_array_sum += cardPoints[i]
            sub_array_sum -= cardPoints[i - (n - k)]
            min_sum = min(min_sum, sub_array_sum)

        return total_sum - min_sum


if __name__ == "__main__":
    assert Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
    assert Solution().maxScore([2, 2, 2], 2) == 4
    assert Solution().maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55
    assert Solution().maxScore([100, 40, 17, 9, 73, 75], 3) == 248
