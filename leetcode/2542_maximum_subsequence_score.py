import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key=lambda x: x[1], reverse=True)  # sort by nums[2] value in decreasing order

        top_k_heap = [x[0] for x in pairs[:k]]  # init the heap
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)  # heap has always the greatest k values of nums

        ans = top_k_sum * pairs[k - 1][1]  # it is sorted in decreasing order, so pairs[k - 1][1] is the min

        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)  # remove the smallest element from the heap (that has k-1 greatest values of nums1) and the sum
            top_k_sum += pairs[i][0]  # Add it to the sum
            heapq.heappush(top_k_heap, pairs[i][0])  # and the heap

            ans = max(ans, top_k_sum * pairs[i][1])  # treat the rest of nums2 elements as the min, update the answer

        return ans


if __name__ == "__main__":
    assert Solution().maxScore(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3) == 12
    assert Solution().maxScore(nums1=[4, 2, 3, 1, 1], nums2=[7, 5, 10, 9, 6], k=1) == 30
