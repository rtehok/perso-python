import collections


class UndergroundSystem:

    def __init__(self):
        self.travel_times = {}
        self.check_ins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, check_in_time = self.check_ins[id]
        travel = (start, stationName)
        travel_time = t - check_in_time
        if travel in self.travel_times:
            total_time, cnt = self.travel_times[travel]
            self.travel_times[travel] = (total_time + travel_time, cnt + 1)
        else:
            self.travel_times[travel] = (travel_time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        total_time, cnt = self.travel_times[travel]
        return total_time / cnt


if __name__ == "__main__":
    us = UndergroundSystem()
    us.checkIn(45, "Leyton", 3)
    # d[Leyton][start][45] = [3]
    us.checkIn(32, "Paradise", 8)
    # d[Paradise][start][32] = [8]
    us.checkIn(27, "Leyton", 10)
    # d[Leyton][start][27] = [10]
    us.checkOut(45, "Waterloo", 15)
    # d[Waterloo][end][45] = [15]
    us.checkOut(27, "Waterloo", 20)
    # d[Waterloo][end][27] = [15]
    us.checkOut(32, "Cambridge", 22)
    # d[Cambridge][end][32] = [15]
    assert us.getAverageTime("Paradise", "Cambridge") == 14
    # (22 - 8) / 1 = 14
    assert us.getAverageTime("Leyton", "Waterloo") == 11
    # ((20 - 10) + (15 - 3)) / 2 = (10 + 12) / 2 = 11
    us.checkIn(10, "Leyton", 24)
    # d[Leyton][start][10] = [24]
    assert us.getAverageTime("Leyton", "Waterloo") == 11
    #  does not change
    us.checkOut(10, "Waterloo", 38)
    # d[Waterloo][end][10] = [38]
    assert us.getAverageTime("Leyton", "Waterloo") == 12
    # ((38 - 24) + 10 + 12) / 3 = (14 + 10 + 12) / 3 = 12

    us = UndergroundSystem()
    us.checkIn(10, "Leyton", 3)
    us.checkOut(10, "Paradise", 8)
    assert us.getAverageTime("Leyton", "Paradise") == 5
    us.checkIn(5, "Leyton", 10)
    us.checkOut(5, "Paradise", 16)
    assert us.getAverageTime("Leyton", "Paradise") == 5.5
    us.checkIn(2, "Leyton", 21)
    us.checkOut(2, "Paradise", 30)
    assert us.getAverageTime("Leyton", "Paradise") == (5 + 6 + 9) / 3
