class Solution:
    def kthGrammarTLE(self, n: int, k: int) -> int:
        res = "0"
        for _ in range(n - 1):
            tmp = ""
            for i in range(len(res)):
                if res[i] == "0":
                    tmp += "01"
                else:
                    tmp += "10"
            res = tmp

        return int(res[k - 1])

    def kthGrammarRecursive(self, n: int, k: int) -> int:
        def solve(n, k):
            if n == 1:
                return 0

            total_elements = 2 ** (n - 1)
            half_elements = total_elements // 2

            if k > half_elements:
                # opposite of precedent row, which is the same first half of current row
                return 1 - solve(n, k - half_elements)

            return solve(n - 1, k)

        return solve(n, k)

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        symbol = 1
        for curr_row in range(n, 1, -1):
            total_elements = 2 ** (curr_row - 1)
            half_elements = total_elements // 2

            if k > half_elements:
                symbol = 1 - symbol
                k -= half_elements

        if symbol != 0:
            return 0

        return 1


if __name__ == "__main__":
    assert Solution().kthGrammar(n=30, k=434991989) == 0
    assert Solution().kthGrammar(n=1, k=1) == 0
    assert Solution().kthGrammar(n=2, k=1) == 0
    assert Solution().kthGrammar(n=2, k=2) == 1
