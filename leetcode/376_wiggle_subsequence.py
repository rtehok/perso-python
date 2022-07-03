from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # n = len(nums)
        # up = [1] * n
        # down = [1] * n
        # for i in range(1, n):
        #     if nums[i] > nums[i - 1]:  # wiggle up
        #         up[i] = down[i - 1] + 1
        #         down[i] = down[i - 1]
        #     elif nums[i] < nums[i - 1]:  # wiggle down
        #         down[i] = up[i - 1] + 1
        #         up[i] = up[i - 1]
        #     else:  # no wiggling
        #         down[i] = down[i - 1]
        #         up[i] = up[i - 1]
        #
        # return max(up[-1], down[-1])

        """DP space optimized"""
        # n = len(nums)
        #
        # if n < 2:
        #     return n
        #
        # up, down = 1, 1
        #
        # for i in range(1, n):
        #     if nums[i] > nums[i - 1]:  # wiggle up
        #         up = down + 1
        #     elif nums[i] < nums[i - 1]:  # wiggle down
        #         down = up + 1
        #
        # return max(up, down)

        """Greedy"""
        n = len(nums)

        if n < 2:
            return n

        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1

        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff

        return count


if __name__ == "__main__":
    assert Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
    assert Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert Solution().wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
