import collections
from typing import List


class Solution:
    def longestPath(self, parents: List[int], s: str) -> int:
        longest_path = 1

        children = collections.defaultdict(list)

        for i, p in enumerate(parents):
            children[p].append(i)

        def dfs(node):
            nonlocal longest_path

            if node not in children:  # is a leaf
                return 1

            longest_chain, longest_second_chain = 0, 0
            for child in children[node]:
                longest_chain_starting_from_node = dfs(child)

                if s[node] == s[child]:
                    continue

                if longest_chain_starting_from_node > longest_chain:
                    longest_second_chain = longest_chain
                    longest_chain = longest_chain_starting_from_node
                elif longest_chain_starting_from_node > longest_second_chain:
                    longest_second_chain = longest_chain_starting_from_node

            longest_path = max(longest_path, 1 + longest_chain + longest_second_chain)
            return longest_chain + 1

        dfs(0)

        return longest_path


if __name__ == "__main__":
    assert Solution().longestPath(parents=[-1, 0, 0, 1, 1, 2], s="abacbe") == 3
    assert Solution().longestPath(parents=[-1, 0, 0, 0], s="aabc") == 3
