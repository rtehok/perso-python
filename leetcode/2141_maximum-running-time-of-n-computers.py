from typing import List


class Solution:
    def maxRunTimeGreedy(self, n: int, batteries: List[int]) -> int:
        # Get the sum of all extra batteries.
        batteries.sort()
        extra = sum(batteries[:-n])

        # live stands for the n largest batteries we chose for n computers.

        live = batteries[-n:]

        # We increase the total running time using 'extra' by increasing
        # the running time of the computer with the smallest battery.
        for i in range(n - 1):
            # If the target running time is between live[i] and live[i + 1].
            if extra // (i + 1) < live[i + 1] - live[i]:
                return live[i] + extra // (i + 1)

            # Reduce 'extra' by the total power used.
            extra -= (i + 1) * (live[i + 1] - live[i])

        # If there is power left, we can increase the running time
        # of all computers.
        return live[-1] + extra // n

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n

        while left < right:
            target = right - (right - left) // 2

            extra = 0
            for power in batteries:
                extra += min(power, target)

            if extra // n >= target:
                left = target
            else:
                right = target - 1

        return left


if __name__ == "__main__":
    assert Solution().maxRunTime(n=2, batteries=[1, 1, 1, 1]) == 2
    assert Solution().maxRunTime(n=2, batteries=[3, 3, 3]) == 4
