from typing import List


class Solution:
    def maximumHappinessSumV0(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = []
        for i, x in enumerate(happiness):
            ans.append(max(0, x - i))

        return sum(ans[:k])

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0

        for i in range(k):
            ans += max(happiness[i] - i, 0)

        return ans


assert Solution().maximumHappinessSum(happiness=[1, 2, 3], k=2) == 4
assert Solution().maximumHappinessSum(happiness=[1, 1, 1, 1], k=2) == 1
assert Solution().maximumHappinessSum(happiness=[2, 3, 4, 5], k=1) == 5
