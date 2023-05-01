from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / (len(salary) - 2)


if __name__ == "__main__":
    assert Solution().average([4000, 3000, 1000, 2000]) == 2500.0
    assert Solution().average([1000, 2000, 3000]) == 2000.0
