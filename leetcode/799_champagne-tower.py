class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * k for k in range(1, 102)]
        glasses[0][0] = poured  # top glass
        for r in range(query_row + 1):
            for c in range(r + 1):
                remaining = (glasses[r][c] - 1.0) / 2.0
                if remaining > 0:
                    # distribute remaining into next 2 glasses
                    glasses[r + 1][c] += remaining
                    glasses[r + 1][c + 1] += remaining
        return min(1, glasses[query_row][query_glass])


if __name__ == "__main__":
    assert Solution().champagneTower(poured=1, query_row=1, query_glass=1) == 0
    assert Solution().champagneTower(poured=2, query_row=1, query_glass=1) == 0.5
    assert Solution().champagneTower(poured=100000009, query_row=33, query_glass=17) == 1
