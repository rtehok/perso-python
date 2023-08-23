import collections
import heapq


class Solution:
    def reorganizeStringHeap(self, s: str) -> str:
        res = []

        q = [(-count, char) for char, count in collections.Counter(s).items()]
        heapq.heapify(q)

        while q:
            cnt_first, c_first = heapq.heappop(q)
            if not res or c_first != res[-1]:
                res.append(c_first)
                if cnt_first + 1 != 0:
                    heapq.heappush(q, (cnt_first + 1, c_first))
            else:
                if not q:
                    return ""
                cnt_second, c_second = heapq.heappop(q)
                res.append(c_second)
                if cnt_second + 1 != 0:
                    heapq.heappush(q, (cnt_second + 1, c_second))
                heapq.heappush(q, (cnt_first, c_first))

        return "".join(res)

    def reorganizeString(self, s: str) -> str:
        char_counts = collections.Counter(s)
        max_cnt, letter = 0, ""

        for char, count in char_counts.items():
            if count > max_cnt:
                max_cnt = count
                letter = char

        if max_cnt > (len(s) + 1) // 2:
            return ""

        ans = [""] * len(s)
        index = 0

        while char_counts[letter] > 0:
            ans[index] = letter
            index += 2
            char_counts[letter] -= 1

        for char, count in char_counts.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1

        return "".join(ans)


if __name__ == "__main__":
    assert Solution().reorganizeString(s="aab") == "aba"
    assert Solution().reorganizeString(s="aaab") == ""
