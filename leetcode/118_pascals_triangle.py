from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            last_row = res[-1]
            new_row = [1]

            for j in range(1, i):
                new_row.append(last_row[j] + last_row[j-1])

            new_row.append(1)

            res.append(new_row)

        return res


if __name__ == "__main__":
    assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert Solution().generate(1) == [[1]]
    assert Solution().generate(2) == [[1], [1, 1]]
