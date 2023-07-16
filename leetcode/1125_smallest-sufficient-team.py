from typing import List


class Solution:
    def smallestSufficientTeamBottomUp(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)

        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i

        skills_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]

        dp = [(1 << n) - 1] * (1 << m)

        dp[0] = 0

        for skills_mask in range(1, 1 << m):
            for i in range(n):
                smaller_skill_mask = skills_mask & ~skills_mask_of_person[i]

                if smaller_skill_mask != skills_mask:
                    people_mask = dp[smaller_skill_mask] | (1 << i)
                    if bin(people_mask).count("1") < bin(dp[skills_mask]).count("1"):
                        dp[skills_mask] = people_mask

        answer_mask = dp[(1 << m) - 1]
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)

        return ans

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)

        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i

        skill_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skill_mask_of_person[i] |= 1 << skill_id[skill]

        dp = [-1] * (1 << m)
        dp[0] = 0

        def dfs(skills_mask):
            if dp[skills_mask] != -1:
                return dp[skills_mask]

            for i in range(n):
                new_skill_mask = skills_mask & ~skill_mask_of_person[i]
                if new_skill_mask != skills_mask:
                    people_mask = dfs(new_skill_mask) | (1 << i)
                    if dp[skills_mask] == -1 or bin(people_mask).count("1") < bin(dp[skills_mask]).count("1"):
                        dp[skills_mask] = people_mask

            return dp[skills_mask]

        answer_mask = dfs((1 << m) - 1)
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)

        return ans


if __name__ == "__main__":
    assert Solution().smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"],
                                             people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]) == [0, 2]
    assert Solution().smallestSufficientTeam(req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                                             people=[["algorithms", "math", "java"], ["algorithms", "math", "reactjs"],
                                                     ["java", "csharp", "aws"], ["reactjs", "csharp"],
                                                     ["csharp", "math"], ["aws", "java"]]) == [1, 2]
