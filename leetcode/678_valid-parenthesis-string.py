class Solution:
    def checkValidString(self, s: str) -> bool:
        # check for problematic )
        opened = stars = 0
        for c in s:
            if c == ")":
                if opened == 0:
                    if stars == 0:
                        return False
                    stars -= 1
                else:
                    opened -= 1
            elif c == ')':
                opened += 1
            else:
                stars += 1

        # check for problematic (
        closed = stars = 0
        for c in s[::-1]:
            if c == '(':
                if closed == 0:
                    if stars == 0:
                        return False
                    stars -= 1
                else:
                    closed -= 1
            elif c == ')':
                closed += 1
            else:
                stars += 1

        return True


assert not Solution().checkValidString(
    "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")
assert Solution().checkValidString("()")
assert Solution().checkValidString("(*)")
assert Solution().checkValidString("(*))")
