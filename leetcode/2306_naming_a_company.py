from typing import List


class Solution:
    def distinctNamesTLE(self, ideas: List[str]) -> int:
        d = set(ideas)

        created = set()

        for i, idea_a in enumerate(ideas):
            for idea_b in ideas[:i] + ideas[i + 1:]:
                part_1 = f"{idea_b[0]}{idea_a[1:]}"
                part_2 = f"{idea_a[0]}{idea_b[1:]}"
                created_name = f"{part_1} {part_2}"
                if part_1 not in d and part_2 not in d:
                    created.add(created_name)

        return len(created)

    def distinctNames(self, ideas: List[str]) -> int:
        initial_groups = [set() for _ in range(26)]
        for idea in ideas:
            initial_groups[ord(idea[0]) - ord('a')].add(idea[1:])

        ans = 0

        for i in range(25):
            for j in range(i, 26):
                num_of_mutual = len(initial_groups[i] & initial_groups[j])
                ans += 2 * (len(initial_groups[i]) - num_of_mutual) * (len(initial_groups[j]) - num_of_mutual)

        return ans


if __name__ == "__main__":
    assert Solution().distinctNames(["coffee", "donuts", "time", "toffee"]) == 6
    assert Solution().distinctNames(["lack", "back"]) == 0
