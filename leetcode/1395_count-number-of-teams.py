from typing import List


class Solution:
    def numTeamsMemo(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        increasing_cache = [[-1] * 4 for _ in range(n)]
        decreasing_cache = [[-1] * 4 for _ in range(n)]

        def count_increasing_teams(curr_idx, team_size):
            if curr_idx == n:
                return 0

            if team_size == 3:
                return 1

            if increasing_cache[curr_idx][team_size] != -1:
                return increasing_cache[curr_idx][team_size]

            valid_teams = 0

            for next_idx in range(curr_idx + 1, n):
                if rating[next_idx] > rating[curr_idx]:
                    valid_teams += count_increasing_teams(next_idx, team_size + 1)

            increasing_cache[curr_idx][team_size] = valid_teams
            return valid_teams

        def count_decreasing_teams(curr_idx, team_size):
            if curr_idx == n:
                return 0

            if team_size == 3:
                return 1

            if decreasing_cache[curr_idx][team_size] != -1:
                return decreasing_cache[curr_idx][team_size]

            valid_teams = 0

            for next_idx in range(curr_idx + 1, n):
                if rating[next_idx] < rating[curr_idx]:
                    valid_teams += count_decreasing_teams(next_idx, team_size + 1)

            decreasing_cache[curr_idx][team_size] = valid_teams
            return valid_teams

        for start_idx in range(n):
            teams += count_increasing_teams(start_idx, 1)
            teams += count_decreasing_teams(start_idx, 1)

        return teams

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        increasing_teams = [[0] * 4 for _ in range(n)]
        decreasing_teams = [[0] * 4 for _ in range(n)]

        for i in range(n):
            increasing_teams[i][1] = 1
            decreasing_teams[i][1] = 1

        for count in range(2, 4):
            for i in range(n):
                for j in range(i + 1, n):
                    if rating[j] > rating[i]:
                        increasing_teams[j][count] += increasing_teams[i][count - 1]
                    if rating[j] < rating[i]:
                        decreasing_teams[j][count] += decreasing_teams[i][count - 1]

        for i in range(n):
            teams += increasing_teams[i][3] + decreasing_teams[i][3]

        return teams


assert Solution().numTeams(rating=[2, 5, 3, 4, 1]) == 3
assert Solution().numTeams(rating=[2, 1, 3]) == 0
assert Solution().numTeams(rating=[1, 2, 3, 4]) == 4
