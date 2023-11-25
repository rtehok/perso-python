from typing import List


class Solution:
    def getSumAbsoluteDifferencesTLE(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            curr = 0
            for j in range(len(nums)):
                curr += abs(nums[i] - nums[j])
            ans.append(curr)

        return ans

    def getSumAbsoluteDifferencesPrefix(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])

        ans = []
        for i in range(n):
            left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]

            left_count = i
            right_count = n - 1 - i

            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            ans.append(left_total + right_total)

        return ans

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        ans = []

        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            left_count = i
            right_count = n - 1 - i
            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]
            ans.append(left_total + right_total)
            left_sum += nums[i]

        return ans


if __name__ == "__main__":
    assert Solution().getSumAbsoluteDifferences(nums=[2, 3, 5]) == [4, 3, 5]
    assert Solution().getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]) == [24, 15, 13, 15, 21]
