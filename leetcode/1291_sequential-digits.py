from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        i = 1
        res = []
        while i <= 8:
            tmp = i
            ans = i
            while ans < high and ans % 10 != 0:
                ans *= 10
                ans += i + 1
                i += 1
                if low <= ans <= high and ans % 10 != 0:
                    res.append(ans)

            i = tmp + 1
        return sorted(res)


assert Solution().sequentialDigits(58, 155) == [67, 78, 89, 123]
assert Solution().sequentialDigits(low=1000, high=13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345]
assert Solution().sequentialDigits(100, 300) == [123, 234]
