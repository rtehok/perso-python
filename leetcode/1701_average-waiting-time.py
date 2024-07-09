from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        next_idle_time = 0
        net_waiting_time = 0

        for customer in customers:
            next_idle_time = max(customer[0], next_idle_time) + customer[1]  # time of delivery
            net_waiting_time += next_idle_time - customer[0]  # waiting time is difference between delivery time and arrival

        return net_waiting_time / n


assert Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]]) == 5.0
assert Solution().averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]) == 3.25000
