from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        res = 0
        i, j = 0, len(people) - 1

        while i <= j:
            res += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1

        return res


if __name__ == "__main__":
    assert Solution().numRescueBoats([5, 1, 4, 2], 6) == 2
    assert Solution().numRescueBoats(people=[1, 2], limit=3) == 1
    assert Solution().numRescueBoats(people=[3, 2, 2, 1], limit=3) == 3
    assert Solution().numRescueBoats(people=[3, 5, 3, 4], limit=5) == 4
