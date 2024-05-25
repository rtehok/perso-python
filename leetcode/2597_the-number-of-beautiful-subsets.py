class Solution:
    def beautifulSubsetsMask(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def dfs(idx, mask):
            if idx == n:
                return 1 if mask > 0 else 0

            isBeautiful = True

            # previous number in subset
            for j in range(idx):
                if ((1 << j) & mask) == 0 or abs(nums[j] - nums[idx]) != k:
                    continue
                else:
                    isBeautiful = False
                    break

            skip = dfs(idx + 1, mask)
            take = dfs(idx + 1, mask + (1 << idx)) if isBeautiful else 0

            return skip + take

        return dfs(0, 0)

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)
        nums.sort()
        n = len(nums)

        def dfs(i):
            # return 1 for subset of size 1
            if i == n:
                return 1

            total_count = dfs(i + 1)

            if nums[i] - k not in freq_map:
                freq_map[nums[i]] += 1
                total_count += dfs(i + 1)
                freq_map[nums[i]] -= 1

                if freq_map[nums[i]] == 0:
                    del freq_map[nums[i]]

            return total_count

        return dfs(0) - 1


assert Solution().beautifulSubsets(nums=[2, 4, 6], k=2) == 4
assert Solution().beautifulSubsets(nums=[1], k=1) == 1
