from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()
        for num in nums:
            integers.add(int(num, 2))

        n = len(nums)
        for num in range(n + 1):
            if num not in integers:
                ans = bin(num)[2:]
                return "0" * (n - len(ans)) + ans

        return ""


if __name__ == "__main__":
    assert Solution().findDifferentBinaryString(["01", "10"]) == "00"
    assert Solution().findDifferentBinaryString(["00", "01"]) == "10"
    assert Solution().findDifferentBinaryString(["111", "011", "001"]) == "000"
