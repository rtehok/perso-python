from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            last = res[-1]
            next_row = [1] * (len(res[-1]) + 1)
            for j in range(1, len(next_row) - 1):
                next_row[j] = last[j - 1] + last[j]
            res.append(next_row)

        return res[:numRows]


if __name__ == "__main__":
    assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert Solution().generate(1) == [[1]]
    assert Solution().generate(2) == [[1], [1, 1]]
