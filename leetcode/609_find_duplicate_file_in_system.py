from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for files in paths:
            ss = files.split(" ")
            r = ss[0]

            for file in ss[1:]:
                name, content = file.split("(")
                d[content].append(f"{r}/{name}")

        return [x for x in d.values() if len(x) > 1]


if __name__ == "__main__":
    assert Solution().findDuplicate(
        ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]) == [
               ['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']]
    assert Solution().findDuplicate(
        ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]) == [
               ['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt']]
    assert Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]) == []
