import collections
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        key_set, lock_set = set(), set()

        moves = {(-1, 0), (0, -1), (1, 0), (0, 1)}

        start_x, start_y = 0, 0

        q = collections.deque()

        all_keys = 0

        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                if curr == '@':
                    start_x, start_y = i, j
                if curr in "abcdef":
                    all_keys += (1 << (ord(curr) - ord("a")))
                    key_set.add(curr)
                if curr in "ABCDEF":
                    lock_set.add(curr)

        seen = collections.defaultdict(set)  # keep state of keys
        seen[0].add((start_x, start_y))

        q.append((start_x, start_y, 0, 0))

        while q:
            i, j, keys, dist = q.popleft()

            for dx, dy in moves:
                nx = i + dx
                ny = j + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                    cell = grid[nx][ny]
                    if cell in key_set and not (keys & (1 << ord(cell) - ord('a'))):  # key not picked up yet
                        new_keys = (keys | (1 << (ord(cell) - ord("a"))))  # pick it up

                        if new_keys == all_keys:
                            return dist + 1

                        seen[new_keys].add((nx, ny))
                        q.append((nx, ny, new_keys, dist + 1))

                    elif cell in lock_set and not (keys & (1 << (ord(cell) - ord("A")))):  # lock that does not have key picked up yet
                        continue

                    elif (nx, ny) not in seen[keys]:  # walk the cell, because we are allowed (not seen yet for this state)
                        seen[keys].add((nx, ny))
                        q.append((nx, ny, keys, dist + 1))

        return -1


if __name__ == "__main__":
    assert Solution().shortestPathAllKeys(["@...a", ".###A", "b.BCc"]) == 10
    assert Solution().shortestPathAllKeys(["@.a..", "###.#", "b.A.B"]) == 8
    assert Solution().shortestPathAllKeys(["@..aA", "..B#.", "....b"]) == 6
    assert Solution().shortestPathAllKeys(["@Aa"]) == -1
