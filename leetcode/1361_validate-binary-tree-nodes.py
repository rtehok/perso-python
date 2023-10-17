import collections
from typing import List


class Solution:
    def validateBinaryTreeNodesV1(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for i in range(n):
            if leftChild[i] >= 0:
                graph[i].append(leftChild[i])
                indegree[leftChild[i]] += 1

            if rightChild[i] >= 0:
                graph[i].append(rightChild[i])
                indegree[rightChild[i]] += 1

        nb_of_root = 0
        for i in range(n):
            if indegree[i] == 0:
                nb_of_root += 1
            if nb_of_root > 1:
                return False

        seen = {0}
        q = collections.deque([0])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append(neighbor)
                    else:
                        return False

        return True

    def validateBinaryTreeNodesDFS(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def findRoot():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i

            return - 1

        root = findRoot()
        if root == -1:
            return False

        seen = {root}
        stack = [root]

        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False

                    seen.add(child)
                    stack.append(child)

        return len(seen) == n

    def validateBinaryTreeNodesBFS(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def findRoot():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i

            return - 1

        root = findRoot()
        if root == -1:
            return False

        seen = {root}
        q = collections.deque([root])

        while q:
            node = q.popleft()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False

                    seen.add(child)
                    q.append(child)

        return len(seen) == n

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        dsu = DSU(n)

        for node in range(n):
            for child in [leftChild[node], rightChild[node]]:
                if child == -1:
                    continue

                if not dsu.union(node, child):
                    return False

        return dsu.components == 1


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.components = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, parent, child):
        parent_parent = self.find(parent)
        child_parent = self.find(child)

        if child_parent != child or parent_parent == child_parent:  # already exists
            return False

        self.components -= 1
        self.parent[child_parent] = parent_parent

        return True


if __name__ == "__main__":
    assert not Solution().validateBinaryTreeNodes(n=6, leftChild=[1, -1, -1, 4, -1, -1],
                                                  rightChild=[2, -1, -1, 5, -1, -1])
    assert Solution().validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1])
    assert not Solution().validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1])
    assert not Solution().validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1])
