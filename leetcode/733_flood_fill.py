from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        def set_new_color(r, c, old_color, new_color):
            if r < 0 or r > m - 1 or c < 0 or c > n - 1 or image[r][c] == new_color:
                return

            if image[r][c] == old_color:
                image[r][c] = new_color
                set_new_color(r - 1, c, old_color, new_color)
                set_new_color(r, c - 1, old_color, new_color)
                set_new_color(r + 1, c, old_color, new_color)
                set_new_color(r, c + 1, old_color, new_color)

        if image[sr][sc] == color:
            return image

        set_new_color(sr, sc, image[sr][sc], color)
        return image


if __name__ == "__main__":
    assert Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert Solution().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]
