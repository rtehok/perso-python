from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> set[str]:
        res = set()
        n = len(s)

        def valid(start, length):
            return length == 1 or (s[start] != "0" and (length < 3 or int(s[start:start + length]) <= 255))

        def backtrack(start, dots):
            remaining_length = n - start
            remaining_nb_of_ints = 4 - len(dots)
            if remaining_length > remaining_nb_of_ints * 3 or remaining_length < remaining_nb_of_ints:
                return

            if len(dots) == 3:  # terminal condition
                if valid(start, remaining_length):
                    last = 0
                    ss = ""
                    for dot in dots:
                        ss += s[last: last + dot]
                        last += dot
                        ss += "."
                    ss += s[start:]
                    res.add(ss)

            cur_pos = 1
            while cur_pos <= 3 and cur_pos <= remaining_length:
                dots.append(cur_pos)
                if valid(start, cur_pos):
                    backtrack(start + cur_pos, dots)
                dots.pop()
                cur_pos += 1

        backtrack(0, [])

        return res


if __name__ == "__main__":
    assert Solution().restoreIpAddresses("25525511135") == {"255.255.11.135", "255.255.111.35"}
    assert Solution().restoreIpAddresses("0000") == {"0.0.0.0"}
    assert Solution().restoreIpAddresses("101023") == {"1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"}
