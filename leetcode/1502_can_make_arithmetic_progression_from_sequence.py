from typing import List


class Solution:
    # TC O(n*log(n)) / SC O(n)
    def canMakeArithmeticProgressionV1(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        diff = arr[1] - arr[0]
        for i in range(2, n):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True

    # TC O(n) / SC O(1)
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_value, max_value = min(arr), max(arr)
        n = len(arr)
        if (max_value - min_value) % (n - 1):
            return False

        diff = (max_value - min_value) // (n - 1)
        i = 0
        while i < n:
            # index at the correct place, move i
            if arr[i] == min_value + i * diff:
                i += 1

            elif (arr[i] - min_value) % diff:
                # not an arithmetic sequence
                return False

            else:  # swap
                j = (arr[i] - min_value) // diff
                if arr[i] == arr[j]:  # check if duplicate
                    return False

                arr[i], arr[j] = arr[j], arr[i]

        return True


if __name__ == "__main__":
    assert Solution().canMakeArithmeticProgression([3, 5, 1])
    assert not Solution().canMakeArithmeticProgression([1, 2, 4])
