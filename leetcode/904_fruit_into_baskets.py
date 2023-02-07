from typing import List


class Solution:
    def totalFruitBruteForce(self, fruits: List[int]) -> int:
        max_picked = 0

        n = len(fruits)
        for left in range(n):
            for right in range(left, n):
                basket = set()
                for i in range(left, right + 1):
                    basket.add(fruits[i])

                if len(basket) <= 2:
                    max_picked = max(max_picked, right - left + 1)

        return max_picked

    def totalFruitBruteForceOptimized(self, fruits: List[int]) -> int:
        max_picked = 0

        n = len(fruits)
        for left in range(n):
            basket = set()
            right = left
            while right < n:
                if fruits[right] not in basket and len(basket) == 2:
                    break

                basket.add(fruits[right])
                right += 1

            max_picked = max(max_picked, right - left)

        return max_picked

    # TC: O(n)
    # SC: O(n)
    def totalFruitSuboptimal(self, fruits: List[int]) -> int:
        basket = {}
        left = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            if len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

        # return len(fruits) - left
        return right - left + 1

    # TC: O(n)
    # SC: O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        left = 0
        max_picked = 0

        for right, fruit in enumerate(fruits):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            max_picked = max(max_picked, right - left + 1)

        return max_picked


if __name__ == "__main__":
    assert Solution().totalFruit([1, 2, 1]) == 3
    assert Solution().totalFruit([0, 1, 2, 2]) == 3
    assert Solution().totalFruit([1, 2, 3, 2, 2]) == 4
