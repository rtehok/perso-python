from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: (x[1], x[0]), reverse=True)
        res = 0
        for i in range(len(boxTypes)):
            if truckSize == 0:
                return res
            if boxTypes[i][0] <= truckSize:
                res += boxTypes[i][0] * boxTypes[i][1]
                truckSize = truckSize - boxTypes[i][0]
            else:
                return res + truckSize * boxTypes[i][1]

        return res


if __name__ == "__main__":
    # assert Solution().maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4) == 8
    # assert Solution().maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10) == 91
    assert Solution().maximumUnits([[1, 3], [5, 5], [2, 5], [4, 2], [4, 1], [3, 1], [2, 2], [1, 3], [2, 5], [3, 2]], 35) == 76
