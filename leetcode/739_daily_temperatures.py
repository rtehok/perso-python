from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n2)
        # n = len(temperatures)
        # res = [0] * n
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        #
        # return res
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return res


if __name__ == "__main__":
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0]
