class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        width = abs(sx - fx)
        height = abs(sy - fy)
        if width == 0 and height == 0 and t == 1:
            return False
        return t >= max(width, height)


if __name__ == "__main__":
    assert Solution().isReachableAtTime(sx=1, sy=1, fx=1, fy=1, t=3)
    assert not Solution().isReachableAtTime(sx=1, sy=2, fx=1, fy=2, t=1)
    assert Solution().isReachableAtTime(sx=2, sy=4, fx=7, fy=7, t=6)
    assert not Solution().isReachableAtTime(sx=3, sy=1, fx=7, fy=3, t=3)
