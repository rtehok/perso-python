class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1

        return left << cnt


assert Solution().rangeBitwiseAnd(left=5, right=7) == 4
assert Solution().rangeBitwiseAnd(left=0, right=0) == 0
assert Solution().rangeBitwiseAnd(left=1, right=2147483647) == 0
