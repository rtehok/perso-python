from typing import List


class Solution:
    def minMovesToSeatSort(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(seats)
        ans = 0
        for i in range(n):
            ans += abs(seats[i] - students[i])

        return ans

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_position = max(max(seats), max(students))
        diff = [0] * max_position
        for pos in seats:
            diff[pos - 1] += 1

        for pos in students:
            diff[pos - 1] -= 1

        moves = 0
        unmatched = 0

        for d in diff:
            moves += abs(unmatched)
            unmatched += d

        return moves


assert Solution().minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]) == 4
assert Solution().minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]) == 7
assert Solution().minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]) == 4
