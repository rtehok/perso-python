import collections
import heapq


class Solution:
    def smallestEquivalentStringV1(self, s1: str, s2: str, baseStr: str) -> str:
        res = []

        groups = collections.defaultdict(set)

        for i in range(len(s1)):
            groups[s1[i]].add(s1[i])
            groups[s1[i]].add(s2[i])
            groups[s2[i]].add(s1[i])
            groups[s2[i]].add(s2[i])
            union = groups[s1[i]].union(groups[s2[i]])
            for x in union:
                groups[x] = union

        groups = dict((k, sorted(list(v))) for k, v in groups.items())

        for i in range(len(baseStr)):
            if baseStr[i] in groups:
                res.append(groups[baseStr[i]][0])
            else:
                res.append(baseStr[i])

        return "".join(res)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        res = []

        representative = []

        def find(x):
            if representative[x] == x:
                return x

            representative[x] = find(representative[x])
            return representative[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y:
                return

            if x < y:
                representative[y] = x
            else:
                representative[x] = y

        for i in range(26):
            representative.append(i)

        for i in range(len(s1)):
            union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))

        for i in range(len(baseStr)):
            res.append(chr(find(ord(baseStr[i]) - ord('a')) + ord('a')))

        return "".join(res)


if __name__ == "__main__":
    assert Solution().smallestEquivalentString(s1="parker", s2="morris", baseStr="parser") == "makkek"
    assert Solution().smallestEquivalentString(s1="hello", s2="world", baseStr="hold") == "hdld"
    assert Solution().smallestEquivalentString(s1="leetcode", s2="programs", baseStr="sourcecode") == "aauaaaaada"
