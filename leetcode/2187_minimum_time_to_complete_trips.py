from typing import List


class Solution:
    def minimumTimeBruteForce(self, time: List[int], totalTrips: int) -> int:
        t = 1
        n = len(time)
        sum_trip = 0
        while sum_trip < totalTrips:
            for bus in range(n):
                if t % time[bus] == 0:
                    sum_trip += 1

            if sum_trip >= totalTrips:
                return t

            t += 1

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # search space of valid travel: [min time to travel <--> min time to travel * totalTrips - i.e. the fastest bus do all the travels]
        left, right = min(time), totalTrips * min(time)


        def timeEnough(given_time):
            actual_trips = 0
            for t in time:
                actual_trips += given_time // t

            return actual_trips >= totalTrips

        while left < right:
            mid = (left + right) // 2
            if timeEnough(mid):  # look for the min value of time that allows bus to add a travel
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    assert Solution().minimumTime(time=[1, 2, 3], totalTrips=5) == 3
    assert Solution().minimumTime(time=[2], totalTrips=1) == 2
    assert Solution().minimumTime([5, 10, 10], 9) == 25
