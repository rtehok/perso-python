import collections


class Solution:
    def largestVariance(self, s: str) -> int:
        max_variance = 0
        char_pos = collections.defaultdict(list)

        for i, c in enumerate(s):
            char_pos[c].append(i)

        for a in char_pos.keys():
            for b in char_pos.keys():
                if a == b:
                    continue

                a_idx = b_idx = a_cnt = b_cnt = 0
                A, B = len(char_pos[a]), len(char_pos[b])

                while a_idx < A or b_idx < B:
                    if a_idx < A and (b_idx == B or char_pos[a][a_idx] < char_pos[b][b_idx]):
                        a_cnt += 1
                        a_idx += 1

                    elif b_idx < B:
                        b_cnt += 1
                        b_idx += 1

                    if b_cnt < a_cnt and a_idx < A:  # reset counter
                        a_cnt = b_cnt = 0

                    if a_cnt > 0 < b_cnt:  # update if both of them are > 0
                        max_variance = max(max_variance, b_cnt - a_cnt)

        return max_variance


if __name__ == "__main__":
    assert Solution().largestVariance(s="aababbb") == 3
    assert Solution().largestVariance(s="abcde") == 0
    assert Solution().largestVariance(s="icexiahccknibwuwgi") == 3
