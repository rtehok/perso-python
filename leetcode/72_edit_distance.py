class Solution:
    # TC : O(3 ** max(m,n))
    def minDistanceRecursive(self, word1: str, word2: str) -> int:
        def helper(i, j):  # i: index of word1, j: index of word2
            if i == 0:  # if word1 is empty, need to add remaining chars of word2
                return j
            if j == 0:  # if word2 is empty, need to add remaining chars of word1
                return i

            if word1[i - 1] == word2[j - 1]:
                return helper(i - 1, j - 1)
            else:
                insert_operation = helper(i, j - 1)
                delete_operation = helper(i - 1, j)
                replace_operation = helper(i - 1, j - 1)
                return min(insert_operation, delete_operation, replace_operation) + 1

        return helper(len(word1), len(word2))

    # TC O(m * n)
    # SC O(m * n)
    def minDistanceMemoization(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = [[None] * (n + 1) for _ in range(m + 1)]  # store result to optimize

        def helper(i, j):  # i: index of word1, j: index of word2
            if i == 0:  # if word1 is empty, need to add remaining chars of word2
                return j
            if j == 0:  # if word2 is empty, need to add remaining chars of word1
                return i

            if memo[i][j]:
                return memo[i][j]

            if word1[i - 1] == word2[j - 1]:
                min_edit_distance = helper(i - 1, j - 1)
            else:
                insert_operation = helper(i, j - 1)
                delete_operation = helper(i - 1, j)
                replace_operation = helper(i - 1, j - 1)
                min_edit_distance = min(insert_operation, delete_operation, replace_operation) + 1

            memo[i][j] = min_edit_distance
            return min_edit_distance

        return helper(m, n)

    # TC O(m * n)
    # SC O(m * n)
    def minDistanceDP(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        if m == 0:
            return n
        if n == 0:
            return m

        dp = [[None] * (n + 1) for _ in range(m + 1)]

        #   "" a b q
        # "" 0 1 2 3
        # a  1 0 1    ==> dp[i][j - 1] + 1 (when inserting)
        # b  2
        # c  3

        #   "" a b q
        # "" 0 1 2 3
        # a  1 0 1    ==> dp[i - 1][j] + 1 (when deleting in word1)
        # b  2
        # c  3

        #   "" a b q
        # "" 0 1 2 3
        # a  1 0 1    ==> dp[i - 1][j - 1] + 1 (when replacing)
        # b  2
        # c  3

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[-1][-1]

    # TC O(m * n)
    # SC O(min(m * n))
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)  # m <= n

        if m > n:
            return self.minDistance(word2, word1)

        previous_row = [i for i in range(m + 1)]

        for i in range(1, n + 1):  # we iterate over the longest, to store the shortest
            current_row = [i]  # first column is [0, 1, 2, 3, ...], hence this line
            for j in range(1, m + 1):
                v = min(1 + current_row[j - 1],  # delete char of word1
                        1 + previous_row[j],  # insert char of word2
                        (0 if word1[j - 1] == word2[i - 1] else 1) + previous_row[j - 1]  # replace if necessary
                        )
                current_row.append(v)
            previous_row = current_row

        return previous_row[-1]


if __name__ == "__main__":
    assert Solution().minDistance(word1="horse", word2="ros") == 3
    assert Solution().minDistance(word1="intention", word2="execution") == 5
