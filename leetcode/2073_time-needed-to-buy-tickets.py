import collections
from typing import List


class Solution:
    def timeRequiredToBuyQueue(self, tickets: List[int], k: int) -> int:
        q = collections.deque()

        for i, ticket in enumerate(tickets):
            q.append((ticket, i))

        time_taken = 0
        while q:
            curr, idx = q.popleft()
            curr -= 1
            time_taken += 1
            if idx == k and curr == 0:
                return time_taken

            if curr != 0:
                q.append((curr, idx))

        return time_taken

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                # i-th person is before k-th person
                time += min(tickets[i], tickets[k])
            else:
                # i-th person is after (i > k)
                time += min(tickets[k] - 1, tickets[i])
        return time


assert Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2)
assert Solution().timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0)
