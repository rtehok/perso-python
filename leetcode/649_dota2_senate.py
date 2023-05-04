import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = senate.count("R")
        d_count = len(senate) - r_count

        d_ban, r_ban = 0, 0  # can ban opposite if encountered in the future

        q = collections.deque(senate)
        while r_count and d_count:
            curr = q.popleft()

            if curr == "D":
                if d_ban:
                    d_ban -= 1
                    d_count -= 1
                else:
                    r_ban += 1
                    q.append("D")
            else:
                if r_ban:
                    r_ban -= 1
                    r_count -= 1
                else:
                    d_ban += 1
                    q.append("R")

        return "Radiant" if r_count else "Dire"


if __name__ == "__main__":
    assert Solution().predictPartyVictory("RD") == 'Radiant'
    assert Solution().predictPartyVictory("RDD") == 'Dire'
