class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        string = ""
        for char in s:
            if char == "[":
                stack.append(string)
                stack.append(num)
                string = ""
                num = 0
            elif char == "]":
                num = stack.pop()
                previous_string = stack.pop()
                string = previous_string + num * string
                num = 0
            elif str.isdigit(char):
                num = num * 10 + int(char)
            else:
                string += char

        return string


if __name__ == "__main__":
    assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
    assert Solution().decodeString("3[a2[c]]") == "accaccacc"
    assert Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
