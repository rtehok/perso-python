import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.defaultdict(int)

        max_freq = 0
        for task in tasks:
            freq[task] += 1
            max_freq = max(max_freq, freq[task])

        # The number of tasks that have the same frequency as max_freq
        max_count = sum(1 for f in freq.values() if f == max_freq)

        # Calculate the minimum number of intervals required to complete all tasks.
        # Each interval has a length of (n+1) and can contain either a task or idle time.
        intervals = (max_freq - 1) * (n + 1) + max_count

        # Handle the case where there are more tasks than intervals
        return max(len(tasks), intervals)


if __name__ == "__main__":
    assert Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2) == 8
    assert Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0) == 6
    assert Solution().leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2) == 16
