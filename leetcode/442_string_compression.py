from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0  # first pointer
        res = 0

        while i < n:
            group_len = 1  # second pointer
            chars[res] = chars[i]  # write
            res += 1

            # move second pointer
            while i + group_len < n and chars[i + group_len] == chars[i]:
                group_len += 1

            if group_len > 1:
                str_repr = str(group_len)
                chars[res:res + len(str_repr)] = list(str_repr)
                res += len(str_repr)

            # move first pointer
            i += group_len

        return res


if __name__ == "__main__":
    arr = ["a", "a", "b", "b", "c", "c", "c"]
    assert Solution().compress(arr) == 6
    assert arr == ["a", "2", "b", "2", "c", "3", "c"]
    arr = ["a"]
    assert Solution().compress(arr) == 1
    assert arr == ["a"]
    arr = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert Solution().compress(arr) == 4
    assert arr == ["a", "b", "1", "2", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
