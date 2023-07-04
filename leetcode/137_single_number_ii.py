from typing import List


class Solution:
    def singleNumberV1(self, nums: List[int]) -> int:
        result = 0

        # Iterate over each bit position from 0 to 31
        for i in range(32):
            count = 0

            # Count the number of set bits at the i-th bit position
            for num in nums:
                count += (num >> i) & 1

            # If the count is not a multiple of 3, set the i-th bit in the result
            if count % 3 != 0:
                # Handle negative numbers by converting the result to its two's complement representation
                if i == 31:
                    result -= (1 << 31)
                else:
                    result |= (1 << i)

        return result

    def singleNumberV2(self, nums: List[int]) -> int:
        ones = 0  # tracks the bits that appeared once
        twos = 0  # tracks the bits that appeared twice

        for num in nums:
            # Update 'twos' by adding the bits that appeared twice
            twos |= (ones & num)

            # Update 'ones' by adding the bits that appeared once and removing the bits that appeared twice
            ones ^= num

            # Update 'common_bits' by removing the bits that appeared three times (present in both 'ones' and 'twos')
            common_bits = ~(ones & twos)

            # Remove the bits that appeared three times from 'ones' and 'twos'
            ones &= common_bits
            twos &= common_bits

        return ones

    def singleNumber(self, nums: List[int]) -> int:
        ones = 0  # tracks the bits that appeared once
        twos = 0  # tracks the bits that appeared twice

        for num in nums:
            ones = (ones ^ num) & ~twos  # update ones and remove bits that appear twice
            twos = (twos ^ num) & ~ones  # update twice and remove bits that appear once

        return ones


if __name__ == "__main__":
    assert Solution().singleNumber(nums=[2, 2, 3, 2]) == 3
    assert Solution().singleNumber(nums=[0, 1, 0, 1, 0, 1, 99]) == 99
