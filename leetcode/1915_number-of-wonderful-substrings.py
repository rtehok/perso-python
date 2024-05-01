class Solution:

    def wonderfulSubstrings(self, word: str) -> int:
        freq = {}  # key: bitmask, value: freq of bitmask key
        freq[0] = 1  # empty prefix

        mask = 0
        res = 0

        for c in word:
            bit = ord(c) - ord('a')
            mask ^= (1 << bit)  # flip parity of the c-th bit in the running prefix mask

            # Count smaller prefixes that create substrings with no odd occurring letters
            if mask in freq:
                res += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1

            # Loop through every possible letter that can appear an odd number of times in a substring

            for odd_c in range(10):
                if (mask ^ (1 << odd_c)) in freq:
                    res += freq[mask ^ (1 << odd_c)]

        return res


assert Solution().wonderfulSubstrings("aba") == 4
assert Solution().wonderfulSubstrings("aabb") == 9
assert Solution().wonderfulSubstrings("he") == 2
