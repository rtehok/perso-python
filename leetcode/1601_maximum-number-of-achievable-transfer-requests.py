import itertools
from typing import List


class Solution:
    # TC O(2 ** m * n) / SC O(n + m)
    def maximumRequestsBackTrack(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n  # track in / out transfers
        self.answer = 0

        def maxRequest(idx, cnt):
            if idx == len(requests):
                for i in range(n):
                    # in the end, all transfer sum must be 0
                    if indegree[i] != 0:
                        return
                self.answer = max(self.answer, cnt)
                return

            indegree[requests[idx][0]] += 1
            indegree[requests[idx][1]] -= 1

            maxRequest(idx + 1, cnt + 1)  # consider the request

            indegree[requests[idx][0]] -= 1
            indegree[requests[idx][1]] += 1

            maxRequest(idx + 1, cnt)  # ignore the request

        maxRequest(0, 0)

        return self.answer

    # TC O(2 ** m)
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_requests = 0

        for combinations in itertools.product([0, 1], repeat=len(requests)):
            in_count = [0] * n
            out_count = [0] * n

            for i, (fromi, toi) in enumerate(requests):
                if combinations[i] == 1:
                    out_count[fromi] += 1
                    in_count[toi] += 1

            if in_count == out_count:
                max_requests = max(max_requests, sum(combinations))

        return max_requests


if __name__ == "__main__":
    assert Solution().maximumRequests(n=5, requests=[[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5
    assert Solution().maximumRequests(n=3, requests=[[0, 0], [1, 2], [2, 1]]) == 3
    assert Solution().maximumRequests(n=4, requests=[[0, 3], [3, 1], [1, 2], [2, 0]]) == 4
