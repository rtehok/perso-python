import collections
from typing import List


class Solution:
    # TC O(n**3) / SC O(1)
    def equalPairV1s(self, grid: List[List[int]]) -> int:
        ans = 0

        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][0] == grid[0][j]:
                    r = 0
                    c = 0
                    while r < n and c < n and grid[r][j] == grid[i][c]:
                        r += 1
                        c += 1
                    if r == c == n:
                        ans += 1

        return ans

    # TC O(n**2) / SC O(n**2)
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)

        row_counter = collections.Counter(tuple(row) for row in grid)

        for c in range(n):
            col = tuple(grid[i][c] for i in range(n))
            ans += row_counter[col]

        return ans

    # TC O(n**2) / SC O(n**2)
    def equalPairsTrie(self, grid: List[List[int]]) -> int:
        t = Trie()
        cnt = 0
        n = len(grid)

        for row in grid:
            t.insert(row)

        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            cnt += t.search(col)

        return cnt


class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, arr):
        t = self.trie
        for a in arr:
            if a not in t.children:
                t.children[a] = TrieNode()

            t = t.children[a]  # move
        t.count += 1

    def search(self, arr):
        t = self.trie
        for a in arr:
            if a in t.children:
                t = t.children[a]  # move
            else:
                return 0
        return t.count


if __name__ == "__main__":
    assert Solution().equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1
    assert Solution().equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]) == 3
