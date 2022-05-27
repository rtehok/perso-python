from typing import List

number_to_string = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(sub: str, res: List[str]) -> List[str]:
            if sub:
                return helper(sub[1:], [f"{r}{c}" for r in res for c in number_to_string[sub[0]]])
            else:
                return res

        if not digits:
            return []

        return helper(digits[1:], [c for c in number_to_string[digits[0]]])


if __name__ == "__main__":
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert Solution().letterCombinations("2") == ["a", "b", "c"]
    assert Solution().letterCombinations("") == []
