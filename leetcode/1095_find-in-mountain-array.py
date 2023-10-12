# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        # search peak
        low = 1
        high = length - 2
        while low != high:
            mid = (low + high) // 2
            curr = mountain_arr.get(mid)
            next = mountain_arr.get(mid + 1)
            if curr < next:
                if curr == target:
                    return mid
                if next == target:
                    return mid + 1
                low = mid + 1
            else:
                high = mid

        peak_index = low

        # search left part
        low = 0
        high = peak_index
        while low <= high:
            mid = (low + high) // 2
            curr = mountain_arr.get(mid)
            if curr == target:
                return mid
            elif curr < target:
                low = mid + 1
            else:
                high = mid - 1

        # search right part
        low = peak_index + 1
        high = length - 1
        while low <= high:
            mid = (low + high) // 2
            curr = mountain_arr.get(mid)
            if curr == target:
                return mid
            elif curr > target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
