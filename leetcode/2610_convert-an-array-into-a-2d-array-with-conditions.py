from typing import List


class Solution:
    def findMatrixV1(self, nums: List[int]) -> List[List[int]]:
        cnt = collections.Counter(nums)
        d = collections.defaultdict(list)
        max_freq = 0
        for k, v in cnt.items():
            d[v].append(k)
            max_freq = max(max_freq, v)

        sorted_freq = [(k, v) for k, v in sorted(d.items(), reverse=True)]

        ans = [[] for _ in range(max_freq)]

        for freq, values in sorted_freq:
            for v in values:
                for i in range(freq):
                    ans[i].append(v)

        return ans

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        freq = [0] * (n + 1)
        ans = []

        for c in nums:
            if freq[c] >= len(ans):
                ans.append([])

            ans[freq[c]].append(c)

            freq[c] += 1
        return ans


assert Solution().findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]) == [[1, 3, 4, 2], [1, 3], [1]]
assert Solution().findMatrix(nums=[1, 2, 3, 4]) == [[1, 2, 3, 4]]
