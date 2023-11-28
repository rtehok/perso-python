class Solution:
    def numberOfWaysTopDown(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        cache = [[-1] * 3 for _ in range(len(corridor))]

        def dfs(index, seats):
            if index == len(corridor):
                return 1 if seats == 2 else 0

            if cache[index][seats] != -1:
                return cache[index][seats]

            if seats == 2:
                if corridor[index] == 'S':
                    result = dfs(index + 1, 1)
                else:
                    result = (dfs(index + 1, 0) + dfs(index + 1, 2)) % MOD

            else:
                if corridor[index] == "S":
                    result = dfs(index + 1, seats + 1)
                else:
                    result = dfs(index + 1, seats)

            cache[index][seats] = result
            return cache[index][seats]

        return dfs(0, 0)

    def numberOfWaysBottomUp(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(corridor)
        count = [[-1] * 3 for _ in range(n + 1)]

        # base cases
        count[n][0] = 0
        count[n][1] = 0
        count[n][2] = 1

        for i in range(n - 1, -1, -1):
            if corridor[i] == "S":
                count[i][0] = count[i + 1][1]
                count[i][1] = count[i + 1][2]
                count[i][2] = count[i + 1][1]
            else:
                count[i][0] = count[i + 1][0]
                count[i][1] = count[i + 1][1]
                count[i][2] = (count[i + 1][0] + count[i + 1][2]) % MOD

        return count[0][0]

    def numberOfWaysBUSO(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        zero = 0
        one = 0
        two = 1
        for thing in corridor:
            if thing == "S":
                zero = one
                one, two = two, one
            else:
                two = (two + zero) % MOD

        return zero

    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        nb_ways = 1
        nb_seats = 0
        nb_plants = 0

        for c in corridor:
            if c == "S":
                nb_seats += 1
                if nb_seats > 0 and nb_seats % 2 == 0:
                    nb_ways *= (nb_plants + 1)
                    nb_ways %= MOD
                    nb_plants = 0
            elif nb_seats > 0 and nb_seats % 2 == 0:
                nb_plants += 1

        if nb_seats % 2 != 0 or nb_seats == 0:
            return 0

        return nb_ways


if __name__ == "__main__":
    assert Solution().numberOfWays(corridor="SSPPSPS") == 3
    assert Solution().numberOfWays(corridor="PPSPSP") == 1
    assert Solution().numberOfWays(corridor="S") == 0
