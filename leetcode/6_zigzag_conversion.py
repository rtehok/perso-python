class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        goingDown = True

        row_number = 0
        for i in range(len(s)):
            res[row_number].append(s[i])
            if row_number == numRows - 1 and goingDown:
                goingDown = False
            if row_number == 0 and not goingDown:
                goingDown = True
            if goingDown:
                if row_number + 1 <= numRows - 1:
                    row_number += 1
            else:
                if row_number - 1 >= 0:
                    row_number -= 1

        return "".join(["".join(x) for x in res])


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))
    print(Solution().convert("PAYPALISHIRING", 4))
    print(Solution().convert("AB", 1))
    print(Solution().convert("AB", 1))
