from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def need_days(capacity):
            needed_days = 1
            running_sum = 0
            for w in weights:
                running_sum += w
                if running_sum > capacity:
                    running_sum = w
                    needed_days += 1
            return needed_days

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2   # right - (left - right) // 2 will not work...
            if need_days(mid) > days:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    assert Solution().shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5) == 15
    assert Solution().shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3) == 6
    assert Solution().shipWithinDays(weights=[1, 2, 3, 1, 1], days=4) == 3
