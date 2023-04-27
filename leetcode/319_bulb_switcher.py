import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


if __name__ == "__main__":
    assert Solution().bulbSwitch(0) == 0
    assert Solution().bulbSwitch(1) == 1  # 0 and 1
    assert Solution().bulbSwitch(2) == 1  # 0, 0 -> 1, 1 -> 1, 0
    assert Solution().bulbSwitch(3) == 1  # 0, 0, 0 -> 1, 1, 1 -> 1, 0, 1 -> 1, 0, 0
    assert Solution().bulbSwitch(4) == 2
    # 0, 0, 0, 0  start
    # 1, 1, 1, 1  round 1
    # 1, 0, 1, 0  round 2
    # 1, 0, 0, 0  round 3
    # 1, 0, 0, 1  round 4
    assert Solution().bulbSwitch(10) == 3
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  start
    # 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  round 1
    # 1, 0, 1, 0, 1, 0, 1, 0, 1, 0  round 2
    # 1, 0, 0, 0, 1, 1, 1, 0, 0, 0  round 3
    # 1, 0, 0, 1, 1, 1, 1, 1, 0, 0  round 4
    # 1, 0, 0, 1, 0, 1, 1, 1, 0, 1  round 5
    # 1, 0, 0, 1, 0, 0, 1, 1, 0, 1  round 6
    # 1, 0, 0, 1, 0, 0, 0, 1, 0, 1  round 7
    # 1, 0, 0, 1, 0, 0, 0, 0, 0, 1  round 8
    # 1, 0, 0, 1, 0, 0, 0, 0, 1, 1  round 9
    # 1, 0, 0, 1, 0, 0, 0, 0, 1, 0  round 9
