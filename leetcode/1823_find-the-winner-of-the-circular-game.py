class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1, n + 1))
        start_index = 0
        while len(circle) > 1:
            removal_index = (start_index + k - 1) % len(circle)
            circle.pop(removal_index)
            start_index = removal_index
        return circle[0]


assert Solution().findTheWinner(5, 2) == 3
assert Solution().findTheWinner(6, 5) == 1
