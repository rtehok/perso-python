from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def helper(path, options):
            if len(options) == 0:
                res.append(path)
            else:
                head = options[0]
                tail = options[1:]

                if head.isdigit():
                    helper(f"{path}{head}", tail)
                else:
                    helper(f"{path}{head.lower()}", tail)
                    helper(f"{path}{head.upper()}", tail)

        helper("", s)

        return res


if __name__ == "__main__":
    assert Solution().letterCasePermutation("a1b2") == ["a1b2", "a1B2", "A1b2", "A1B2"]
    assert Solution().letterCasePermutation("3z4") == ["3z4", "3Z4"]
