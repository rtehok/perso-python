class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        s = list(s)
        s2 = list(s)
        s2[0] = "1" if s2[0] == "0" else "0"

        def getNbOp(input, ans):
            prev = input[0]
            for i in range(1, n):
                if input[i] == prev:
                    ans += 1
                    input[i] = "1" if input[i] == "0" else "0"
                    prev = input[i]
                else:
                    prev = input[i]
            return ans

        return min(getNbOp(s, 0), getNbOp(s2, 1))


assert Solution().minOperations("0100") == 1
assert Solution().minOperations("10") == 0
assert Solution().minOperations("1111") == 2
