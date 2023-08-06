class Solution:
    def numMusicPlaylistsBottomUp(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                # Pick a new song
                dp[i][j] += (dp[i][j] + dp[i - 1][j - 1] * (n - j + 1)) % MOD

                # Repeat a song
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD

        return dp[goal][n]

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[-1] * (n + 1) for _ in range(goal + 1)]

        def number_of_playlists(i, j):
            if i == 0 and j == 0:
                return 1
            if i == 0 or j == 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = (number_of_playlists(i - 1, j - 1) * (n - j + 1)) % MOD

            if j > k:
                dp[i][j] += (number_of_playlists(i - 1, j) * (j - k)) % MOD

                dp[i][j] %= MOD

            return dp[i][j]

        return number_of_playlists(goal, n)

if __name__ == "__main__":
    assert Solution().numMusicPlaylists(n = 3, goal = 3, k = 1) == 6
    assert Solution().numMusicPlaylists(n = 2, goal = 3, k = 0) == 6
    assert Solution().numMusicPlaylists(n = 2, goal = 3, k = 1) == 2