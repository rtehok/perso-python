from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        for s in bank:
            cnt = 0
            for c in s:
                if c == "1":
                    cnt += 1

            if cnt > 0:
                ans += prev * cnt
                prev = cnt
        return ans


assert Solution().numberOfBeams(["011001", "000000", "010100", "001000"]) == 8
assert Solution().numberOfBeams(["000", "111", "000"]) == 0
