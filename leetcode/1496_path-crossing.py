class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        coordinates = set()
        coordinates.add((x, y))
        for p in path:
            if p == "N":
                y += 1
            if p == "S":
                y -= 1
            if p == "W":
                x -= 1
            if p == "E":
                x += 1
            if (x, y) in coordinates:
                return True
            coordinates.add((x, y))
        return False


assert not Solution().isPathCrossing("NES")
assert Solution().isPathCrossing("NESWW")