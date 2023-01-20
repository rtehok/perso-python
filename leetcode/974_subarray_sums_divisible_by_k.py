from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_mod = 0
        mod_groups = [0] * k
        mod_groups[0] = 1

        for num in nums:
            prefix_mod = (prefix_mod + num % k + k) % k
            ans += mod_groups[prefix_mod]
            mod_groups[prefix_mod] += 1

        return ans


if __name__ == "__main__":
    assert Solution().subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5) == 7
    assert Solution().subarraysDivByK(nums=[5], k=9) == 0
