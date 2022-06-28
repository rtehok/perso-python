class Solution:
    def minPartitions(self, n: str) -> int:
        # 2 5 9 4 3
        # 1 1 1 1 1
        # 1 1 1 1 1
        # 0 1 1 1 1
        # 0 1 1 1 0
        # 0 1 1 0 0
        # 0 0 1 0 0
        # 0 0 1 0 0
        # 0 0 1 0 0
        # 0 0 1 0 0
        max_val = 0
        for i in range(len(n)):
            val = ord(n[i]) - ord('0')
            if val == 9:
                return 9
            max_val = max(val, max_val)
        return max_val


if __name__ == "__main__":
    assert Solution().minPartitions("32") == 3
    assert Solution().minPartitions("82734") == 8
    assert Solution().minPartitions("27346209830709182346") == 9
