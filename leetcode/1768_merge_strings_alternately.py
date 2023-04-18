class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        res = []
        while i < m or j < n:
            if i < m:
                res.append(word1[i])
                i += 1
            if j < n:
                res.append(word2[j])
                j += 1

        return "".join(res)


if __name__ == "__main__":
    assert Solution().mergeAlternately(word1="abc", word2="pqr") == "apbqcr"
    assert Solution().mergeAlternately(word1="ab", word2="pqrs") == "apbqrs"
    assert Solution().mergeAlternately(word1="abcd", word2="pq") == "apbqcd"
    assert Solution().mergeAlternately(word1="cf", word2="eee") == "cefee"
