from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        m = len(str(k))
        i = 0
        carry = 0
        res = [0] * max(m, n)
        while i < n or i < m or k > 0:
            sum = num[n - 1 - i] + k % 10 + carry if i < n else k % 10 + carry
            res[max(m, n) - 1 - i] = sum % 10
            carry = sum // 10
            k //= 10
            i += 1

        if carry > 0:
            return [carry] + res

        return res


if __name__ == "__main__":
    assert Solution().addToArrayForm(num=[1, 2, 0, 0], k=34) == [1, 2, 3, 4]
    assert Solution().addToArrayForm(num=[2, 7, 4], k=181) == [4, 5, 5]
    assert Solution().addToArrayForm(num=[2, 1, 5], k=806) == [1, 0, 2, 1]
    assert Solution().addToArrayForm(num=[0], k=23) == [2, 3]
    assert Solution().addToArrayForm(num=[0], k=10000) == [1, 0, 0, 0, 0]
