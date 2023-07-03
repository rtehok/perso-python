import collections


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False

        pairs = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                pairs.append((s[i], goal[i]))

        if len(pairs) != 2:
            return False

        return pairs[0] == pairs[1][::-1]


if __name__ == "__main__":
    assert Solution().buddyStrings(s="ab", goal="ba")
    assert not Solution().buddyStrings(s="ab", goal="ab")
    assert Solution().buddyStrings(s="aa", goal="aa")
