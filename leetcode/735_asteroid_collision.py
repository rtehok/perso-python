from typing import List


class Solution:
    def asteroidCollisionV1(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = [asteroids[0]]
        i = 1
        while i < n:
            if stack:
                if (asteroids[i] > 0 and stack[-1] > 0) or (stack[-1] < 0 and asteroids[i] < 0) or (
                        stack[-1] < 0 < asteroids[i]):
                    stack.append(asteroids[i])
                if stack[-1] > 0 > asteroids[i]:

                    destroyed = False

                    while stack and 0 < stack[-1] <= -asteroids[i]:
                        if stack[-1] == -asteroids[i]:
                            stack.pop()
                            destroyed = True
                            break

                        elif 0 < stack[-1] < -asteroids[i]:
                            stack.pop()

                    if not destroyed and asteroids[i] < 0:
                        if (stack and stack[-1] < 0) or not stack:
                            stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])

            i += 1

        return stack

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans


if __name__ == "__main__":
    assert Solution().asteroidCollision([1, -2, -2, -2]) == [-2, -2, -2]
    assert Solution().asteroidCollision([-2, 1, 1, -1]) == [-2, 1]
    assert Solution().asteroidCollision([-2, 1, -1, -2]) == [-2, -2]
    assert Solution().asteroidCollision([-2, -2, 1, -1]) == [-2, -2]
    assert Solution().asteroidCollision([10, 2, -5]) == [10]
    assert Solution().asteroidCollision([-2, -2, 1, -2]) == [-2, -2, -2]
    assert Solution().asteroidCollision([8, -8]) == []
    assert Solution().asteroidCollision([5, 10, -5]) == [5, 10]
    assert Solution().asteroidCollision([-2, -2, -1, -2]) == [-2, -2, -1, -2]
    assert Solution().asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
