class Solution:
    def numStepsV1(self, s: str) -> int:
        steps = 0
        num = int(s, 2)
        while num != 1:
            if num % 2 != 0:
                num += 1
            else:
                num //= 2
            steps += 1

        return steps

    def numStepsGreedy(self, s: str) -> int:
        n = len(s)
        steps = 0
        carry = 0
        for i in range(n - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry

    def numSteps(self, s: str) -> int:
        def divide_by_two(s):
            s.pop()
            return s

        def add_one(s):
            i = len(s) - 1
            while i >= 0 and s[i] != "0":
                s[i] = "0"
                i -= 1

            if i < 0:
                s.insert(0, "1")
            else:
                s[i] = "1"

            return s

        s = list(s)
        steps = 0
        while len(s) > 1:
            if s[len(s) - 1] == "0":  # last char is 0 == even
                s = divide_by_two(s)
            else:
                s = add_one(s)
            steps += 1

        return steps

    # 12 => 1100 ==> // 2
    # 6  => 0110 ==> // 2
    # 3  => 0011 ==> +1
    # 4  => 0100 ==> //2
    # 2  => 0010 ==> //2
    # 1


assert Solution().numSteps("1101") == 6
assert Solution().numSteps("10") == 1
assert Solution().numSteps("1") == 0
