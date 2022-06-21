# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        mid = 1

        while l <= r:
            mid = r - (r - l) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                r = mid - 1
            else:
                l = mid + 1

        return mid
