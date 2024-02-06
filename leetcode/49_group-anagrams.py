import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for i, x in enumerate(strs):
            s = "".join(sorted(x))
            d[s].append(x)
        res = []
        for v in d.values():
            res.append(v)
        return res


assert Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]) == [["bat"], ["nat", "tan"],
                                                                                     ["ate", "eat", "tea"]]
