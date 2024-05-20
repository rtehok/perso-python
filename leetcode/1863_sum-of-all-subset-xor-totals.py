from typing import List


class Solution:
    def subsetXORSumRecursive(self, nums: List[int]) -> int:
        def generate_subsets(idx, curr):
            if idx == len(nums):
                return curr

            with_elt = generate_subsets(idx + 1, curr ^ nums[idx])
            without_elt = generate_subsets(idx + 1, curr)

            return with_elt + without_elt

        return generate_subsets(0, 0)

    def subsetXORSum(self, nums: List[int]) -> int:
        def generate_subsets(idx, subset, subsets):
            if idx == len(nums):
                subsets.append(subset[:])
                return

            # with elt
            subset.append(nums[idx])
            generate_subsets(idx + 1, subset, subsets)
            subset.pop()

            # without elt
            generate_subsets(idx + 1, subset, subsets)

        subsets = []
        generate_subsets(0, [], subsets)

        res = 0
        for subset in subsets:
            subset_XOR_total = 0
            for num in subset:
                subset_XOR_total ^= num
            res += subset_XOR_total

        return res


assert Solution().subsetXORSum(nums=[1, 3]) == 6
assert Solution().subsetXORSum(nums=[5, 1, 6]) == 28
assert Solution().subsetXORSum(nums=[3, 4, 5, 6, 7, 8]) == 480
