from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 1:
            return [1] * (rowIndex + 1)

        prev = [1, 1]
        new_row = []

        for i in range(2, rowIndex + 1):
            new_row = [1]

            for j in range(1, i):
                new_row.append(prev[j] + prev[j - 1])

            new_row.append(1)
            prev = new_row

        return new_row


if __name__ == "__main__":
    assert Solution().getRow(4) == [1, 4, 6, 4, 1]
    assert Solution().getRow(3) == [1, 3, 3, 1]
    assert Solution().getRow(0) == [1]
    assert Solution().getRow(1) == [1, 1]
