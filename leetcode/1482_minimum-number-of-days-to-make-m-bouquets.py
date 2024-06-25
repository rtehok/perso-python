from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def get_number_of_bouquets(mid):
            num_of_bouquet = 0
            count = 0
            for day in bloomDay:
                if day <= mid:
                    count += 1
                else:
                    count = 0

                if count == k:
                    num_of_bouquet += 1
                    count = 0

            return num_of_bouquet

        if m * k > len(bloomDay):
            return -1

        start = 0
        end = max(bloomDay)

        minDays = -1

        while start <= end:
            mid = (start + end) // 2
            if get_number_of_bouquets(mid) >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1

        return minDays


assert Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2) == -1
assert Solution().minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3) == 12
