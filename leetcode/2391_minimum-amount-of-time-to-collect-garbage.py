import collections
from typing import List


class Solution:
    def garbageCollectionV1(self, garbage: List[str], travel: List[int]) -> int:
        max_m_t = max_p_t = max_g_t = 0
        m_count = p_count = g_count = 0
        travel.append(0)
        t = 0
        for i, assort in enumerate(garbage):
            for g in assort:
                if g == 'M':
                    m_count += 1
                    max_m_t = t
                if g == 'G':
                    g_count += 1
                    max_g_t = t
                if g == 'P':
                    p_count += 1
                    max_p_t = t
            t += travel[i]

        return max_m_t + max_p_t + max_g_t + m_count + p_count + g_count

    def garbageCollectionHashMap(self, garbage: List[str], travel: List[int]) -> int:
        max_t = collections.defaultdict(int)
        travel.append(0)
        t = 0
        count = 0
        for i, assort, in enumerate(garbage):
            count += len(assort)
            for g in assort:
                max_t[g] = t
            t += travel[i]

        return count + sum(max_t.values())

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        garbage_last_post = collections.defaultdict(int)
        garbage_cnt = collections.defaultdict(int)

        for i, assort in enumerate(garbage):
            for g in assort:
                garbage_last_post[g] = i
                garbage_cnt[g] += 1

        n = len(travel)
        prefix_time = [0] + [0] * n

        for i in range(1, n + 1):
            prefix_time[i] = travel[i - 1] + prefix_time[i - 1]

        ans = 0
        for g in "MPG":
            if g in garbage_cnt:
                ans += prefix_time[garbage_last_post[g]] + garbage_cnt[g]

        return ans


if __name__ == "__main__":
    assert Solution().garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]) == 21
    assert Solution().garbageCollection(garbage=["MMM", "PGM", "GP"], travel=[3, 10]) == 37
