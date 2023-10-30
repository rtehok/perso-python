import collections
from typing import List


class Solution:
    def sortByBitsV0(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda num: (num.bit_count(), num))
        return arr

    def sortByBitsV1(self, arr: List[int]) -> List[int]:
        d = collections.defaultdict(list)
        arr.sort()
        max_nb_1 = 0
        for x in arr:
            k = bin(x).count("1")
            max_nb_1 = max(max_nb_1, k)
            d[k].append(x)

        res = []
        for i in range(max_nb_1 + 1):
            if i in d:
                res.extend(d[i])

        return res

    def sortByBits(self, arr: List[int]) -> List[int]:
        def find_weight(num):
            mask = 1
            weight = 0
            while num:
                if num & mask:
                    weight += 1
                    num ^= mask

                mask <<= 1

            return weight

        arr.sort(key=lambda num: (find_weight(num), num))
        return arr


if __name__ == "__main__":
    assert Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 4, 8, 3, 5, 6, 7]
    assert Solution().sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 2, 4, 8, 16, 32, 64, 128,
                                                                                        256, 512, 1024]
