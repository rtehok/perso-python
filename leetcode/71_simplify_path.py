class Solution:
    def simplifyPathV1(self, path: str) -> str:
        tmp = path.split("/")
        stack = [""]

        i = 1
        while i < len(tmp):
            folder = tmp[i]
            if folder == "." or folder == "":
                i += 1
                continue

            if folder == "..":
                if len(stack) > 1 or stack[-1] == "..":
                    stack.pop()
                i += 1
                continue

            stack.append(folder)
            i += 1

        return "/".join(stack) if len(stack) > 1 else "/"

    def simplifyPath(self, path: str) -> str:

        path = path.split("/")
        stack = []

        for folder in path:
            if stack and folder == "..":
                stack.pop()
            elif folder not in {"", ".", ".."}:
                stack.append(folder)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    assert Solution().simplifyPath(path="/a/./b/../../c/") == "/c"
    assert Solution().simplifyPath(path="/../") == "/"
    assert Solution().simplifyPath(path="/home/") == "/home"
    assert Solution().simplifyPath(path="/home//foo/") == "/home/foo"
    assert Solution().simplifyPath(path="/a/../../b/../c//.//") == "/c"
