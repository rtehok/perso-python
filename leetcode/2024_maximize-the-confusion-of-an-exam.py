import collections


class Solution:
    # TC O(n * log(n))
    def maxConsecutiveAnswersBinarySearch(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        def isValid(size):
            cnt = collections.Counter(answerKey[:size])
            if min(cnt["T"], cnt["F"]) <= k:
                return True

            for i in range(size, n):  # Moving window
                cnt[answerKey[i]] += 1
                cnt[answerKey[i - size]] -= 1
                if min(cnt["T"], cnt["F"]) <= k:
                    return True
            return False

        left, right = k, n
        while left < right:
            mid = (left + right + 1) // 2
            if isValid(mid):  # at least one window exist of size mid
                left = mid  # too large, so move to the right
            else:
                right = mid - 1  # search on left part [left, mid -1]
        return left

    # Sliding window TC O(n)
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_size = k
        cnt = collections.Counter(answerKey[:k])
        left = 0
        for right in range(k, len(answerKey)):
            cnt[answerKey[right]] += 1

            while min(cnt["T"], cnt["F"]) > k:
                cnt[answerKey[left]] -= 1
                left += 1

            max_size = max(max_size, right - left + 1)

        return max_size


if __name__ == "__main__":
    assert Solution().maxConsecutiveAnswers(answerKey="TTFF", k=2) == 4
    assert Solution().maxConsecutiveAnswers(answerKey="TFFT", k=1) == 3
    assert Solution().maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1) == 5
    assert Solution().maxConsecutiveAnswers(answerKey="FFFTTFTTFT", k=3) == 8
