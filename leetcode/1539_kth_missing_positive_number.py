from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # the number of missing values at i is arr[i] - (i + 1)

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)

            # find the last element in array before kth missing
            if missing < k:
                left = mid + 1  # too small, we need to go right
            else:
                right = mid - 1  # to big, need to go left

        # 1. arr[start - 1] is the last element before the kth missing positive integer, so we start with this value.
        # 1.1 arr[start - 1] - (start - 1) - 1 is the number of missing at start - 1
        # 2. (k - (arr[start - 1] - (start - 1) - 1)) is the number of missing positive integers between arr[start - 1]
        # and the kth missing positive integer.
        # We subtract arr[start - 1] - (start - 1) - 1 from k to account for the missing positive integers before arr[start - 1].
        # We then add this value to arr[start - 1] to get the kth missing positive integer.
        # 3. arr[start - 1] + (k - (arr[start - 1] - (start - 1) - 1)) = start + k

        # return arr[left-1] + (k - (arr[left-1] - ((left - 1) + 1)))
        return left + k


if __name__ == "__main__":
    assert Solution().findKthPositive(arr=[2, 3, 4, 7, 11], k=5) == 9
    assert Solution().findKthPositive(arr=[1, 2, 3, 4], k=2) == 6
