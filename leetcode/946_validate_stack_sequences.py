from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        tmp = []
        i = 0
        for p in pushed:
            tmp.append(p)
            while tmp and tmp[-1] == popped[i]:
                tmp.pop()
                i += 1


        return len(tmp) == 0


if __name__ == "__main__":
    assert Solution().validateStackSequences([2, 1, 0], [1, 2, 0])
    assert Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])
    assert not Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2])
