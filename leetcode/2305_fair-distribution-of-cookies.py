from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        cur = [0] * k

        def dfs(i, zero_count):
            # early-stop optimization: count the number of children that don't have cookies yet
            if n - i < zero_count:
                return float("inf")

            if i == n:
                return max(cur)

            answer = float("inf")

            for j in range(k):
                zero_count -= int(cur[j] == 0)
                cur[j] += cookies[i]

                answer = min(answer, dfs(i + 1, zero_count))

                cur[j] -= cookies[i]
                zero_count += int(cur[j] == 0)

            return answer

        return dfs(0, k)


if __name__ == "__main__":
    assert Solution().distributeCookies(cookies=[8, 15, 10, 20, 8], k=2) == 31
    assert Solution().distributeCookies(cookies=[6, 1, 3, 2, 2, 4, 1, 2], k=3) == 7
