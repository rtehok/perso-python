from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        unrealized_customers = 0

        for i in range(minutes):
            unrealized_customers += customers[i] * grumpy[i]

        max_unrealized_customers = unrealized_customers

        for i in range(minutes, n):
            unrealized_customers += customers[i] * grumpy[i]
            unrealized_customers -= customers[i - minutes] * grumpy[i - minutes]
            max_unrealized_customers = max(max_unrealized_customers, unrealized_customers)

        total_customers = max_unrealized_customers

        for i in range(n):
            total_customers += customers[i] * (1 - grumpy[i])

        return total_customers


assert Solution().maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3) == 16
assert Solution().maxSatisfied(customers=[1], grumpy=[0], minutes=1) == 1
