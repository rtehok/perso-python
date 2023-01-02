from typing import List


class Solution:
    def canCompleteCircuitBruteForce(self, gas: List[int], cost: List[int]) -> int:
        total = 0

        # start by calculating the total remaining gas
        n = len(gas)

        for i in range(n):
            total += gas[i] - cost[i]

        if total < 0:
            return -1

        for i in range(n):
            tank = 0
            round_trip = True
            for j in range(i, i + n + 1):  # go circular
                tank += gas[j % n] - cost[j % n]
                if tank < 0:
                    round_trip = False
                    break
            if round_trip:
                return i

        return -1

    def canCompleteCircuitSubOptimal(self, gas: List[int], cost: List[int]) -> int:
        gas_in_tank = 0
        total = 0
        start = 0

        # start by calculating the total remaining gas
        n = len(gas)

        for i in range(n):
            total += gas[i] - cost[i]

        if total < 0:
            return -1

        # at this point, one starting point exists (otherwise it would be returned -1 at previous step)
        for i in range(n):
            gas_in_tank += gas[i] - cost[i]
            if gas_in_tank < 0:  # as a solution exists, take the last negative remainder and go to next gas station
                start = i + 1
                gas_in_tank = 0  # start empty

        return start

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_in_tank = 0
        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            gas_in_tank += gas[i] - cost[i]
            if gas_in_tank < 0:
                start = i + 1
                gas_in_tank = 0

        return start if total >= 0 else -1


if __name__ == "__main__":
    assert Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3
    assert Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
