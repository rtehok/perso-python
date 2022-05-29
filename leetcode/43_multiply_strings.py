class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            int_a = ord(num1[i]) - ord('0')
            for j in range(len(num2) - 1, -1, -1):
                int_b = ord(num2[j]) - ord('0')
                product = int_a * int_b + res[i + j + 1]
                res[i + j + 1] = product % 10
                res[i + j] += product // 10

        res = res[1:] if res[0] == 0 else res
        return "".join([f"{x}" for x in res])


if __name__ == "__main__":
    assert Solution().multiply("2", "3") == "6"
    assert Solution().multiply("123", "456") == "56088"
