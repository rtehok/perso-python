# Definition for a Node.
import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visit = {node.val: Node(node.val, [])}

        q = collections.deque()
        q.append(node)

        while q:
            cur = q.popleft()
            cur_clone = visit[cur.val]

            for neighbor in cur.neighbors:
                if neighbor.val not in visit:
                    visit[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)

                cur_clone.neighbors.append(visit[neighbor.val])

        return visit[node.val]
