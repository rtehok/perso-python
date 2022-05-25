# game of life
#
# meurt => si < 2
# 1 => 1 : si 2 ou 3 voisins
# surpopulation = 4 + ==> meurt
# si 3 voisins actifs => meurt ==> vivant
# voisins => 8 cases adjacentes
from typing import List


def game(arr: List[List[int]]) -> List[List[int]]:
    m = len(arr)
    n = len(arr[0])

    moves = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    # res = [[-1] * n for _ in range(m)]
    buff = []

    def set_next_state(r, c):
        alive = 0
        for move in moves:
            x = r + move[0]
            y = c + move[1]
            if 0 <= x <= m - 1 and 0 <= y <= n - 1 and arr[x][y]:
                alive += 1
        if alive < 2 or alive >= 4:
            # print(r, c, alive, 0)
            buff.append(0)
            # res[r][c] = 0
        elif (2 <= alive <= 3 and arr[r][c]) or (alive == 3 and not arr[r][c]):
            # print(r, c, alive, 1)
            buff.append(1)
            # res[r][c] = 1
        else:
            # print(r, c, alive, 1)
            buff.append(arr[r][c])
            # res[r][c] = arr[r][c]

    x = 0
    y = 0
    for i in range(m):
        for j in range(n):
            set_next_state(i, j)
            if i >= 1:
                if i == 1 and j < 2:
                    continue
                x = i - 1 if j >= 2 or i == 1 else i - 2
                y = (j - 2) % n
                # print(x, y, buff)
                arr[x][y] = buff.pop(0)

    i = x
    j = y
    while buff:
        arr[i][j] = buff.pop(0)
        j = (j + 1) % n
        i = i + 1 if j == 0 else i

    return arr
    # return res


if __name__ == "__main__":
    arr = [
        [0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0]
    ]
    # [[0, 0, 0, 0, 0],
    # [1, 0, 1, 1, 0],
    # [1, 0, 0, 0, 0],
    # [1, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0]]
    print(game(arr))
