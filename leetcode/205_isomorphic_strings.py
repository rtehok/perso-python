class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 not in s_dict) and (c2 not in t_dict):
                s_dict[c1] = c2
                t_dict[c2] = c1
            elif s_dict.get(c1) != c2 or t_dict.get(c2) != c1:
                return False

        return True


if __name__ == "__main__":
    assert Solution().isIsomorphic("egg", "add")
    assert not Solution().isIsomorphic("foo", "bar")
    assert Solution().isIsomorphic("paper", "title")
    assert not Solution().isIsomorphic("badc", "baba")
