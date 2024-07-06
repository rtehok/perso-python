class Solution:
    def passThePillowSimulation(self, n: int, time: int) -> int:
        pos = 1
        curr_time = 0
        dir = 1
        while curr_time < time:
            if 0 < pos + dir <= n:
                pos += dir
                curr_time += 1
            else:
                dir *= -1
        return pos

    def passThePillow(self, n: int, time: int) -> int:
        nb_round = time // (n - 1)
        extra_time = time % (n - 1)

        if nb_round % 2 == 0:
            return extra_time + 1
        else:
            return n - extra_time


assert Solution().passThePillow(3, 2) == 3
assert Solution().passThePillow(4, 5) == 2
assert Solution().passThePillow(8, 9) == 6
