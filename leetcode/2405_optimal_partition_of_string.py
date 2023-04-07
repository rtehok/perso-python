class Solution:
    def partitionStringV1(self, s: str) -> int:
        a = [0] * 26

        res = 1
        for l in s:
            letter_index = ord(l) - ord('a')

            if a[letter_index] >= 1:
                res += 1
                a = [0] * 26

            a[letter_index] += 1

        return res

    def partitionStringV2(self, s: str) -> int:
        last_seen = [-1] * 26

        res = 1
        substring_start = 0
        for i, l in enumerate(s):
            letter_index = ord(l) - ord('a')

            if last_seen[letter_index] >= substring_start:
                res += 1
                substring_start = i

            last_seen[letter_index] = i

        return res

    def partitionString(self, s: str) -> int:
        last_seen = set()

        res = 1
        for i, l in enumerate(s):
            letter_index = ord(l) - ord('a')

            if letter_index in last_seen:
                res += 1
                last_seen = set()

            last_seen.add(letter_index)

        return res


if __name__ == "__main__":
    assert Solution().partitionString("abacaba") == 4
    assert Solution().partitionString("ssssss") == 6
    assert Solution().partitionString("hdklqkcssgxlvehva") == 4
