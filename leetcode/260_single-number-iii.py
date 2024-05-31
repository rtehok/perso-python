from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all the elements
        xor_all = 0
        for num in nums:
            xor_all ^= num

        # Step 2: Find a set bit in the result
        set_bit = 1
        while (xor_all & set_bit) == 0:
            set_bit <<= 1

        # Step 3: Divide the array into two groups and XOR each group
        num1 = 0
        num2 = 0
        for num in nums:
            if (num & set_bit) == 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


assert Solution().singleNumber([1, 2, 1, 3, 2, 5]) == [5, 3]
assert Solution().singleNumber([-1, 0]) == [0, -1]
assert Solution().singleNumber([0, 1]) == [0, 1]
