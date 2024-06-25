from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def can_place_balls(x):
            prev_ball_position = position[0]
            balls_placed = 1

            for i in range(1, n):
                curr_pos = position[i]
                if curr_pos - prev_ball_position >= x:
                    balls_placed += 1
                    prev_ball_position = curr_pos

                if balls_placed == m:
                    return True

            return False

        ans = 0
        left = 1
        right = position[-1] // (m - 1) + 1

        while left <= right:
            mid = (left + right) // 2
            if can_place_balls(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


assert Solution().maxDistance(position=[1, 2, 3, 4, 7], m=3) == 3
assert Solution().maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2) == 999999999
