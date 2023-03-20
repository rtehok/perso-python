from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or flowerbed[i - 1] == 0
                empty_right = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n


if __name__ == "__main__":
    assert Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1)
    assert not Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2)
    assert not Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2)
