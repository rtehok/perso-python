from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_ability = max(worker)
        jobs = [0] * (max_ability + 1)
        for i in range(len(difficulty)):
            if difficulty[i] <= max_ability:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])

        for i in range(1, max_ability + 1):
            jobs[i] = max(jobs[i], jobs[i - 1])

        net_profit = 0
        for ability in worker:
            net_profit += jobs[ability]

        return net_profit


assert Solution().maxProfitAssignment(difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50],
                                      worker=[4, 5, 6, 7]) == 100
assert Solution().maxProfitAssignment(difficulty=[85, 47, 57], profit=[24, 66, 99], worker=[40, 25, 25]) == 0
