import heapq


class SeatManager:

    def __init__(self, n: int):
        self.available_seats = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        seat_number = heapq.heappop(self.available_seats)
        return seat_number

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self.available_seats, seat_number)


if __name__ == "__main__":
    manager = SeatManager(5)
    assert manager.reserve() == 1
    assert manager.reserve() == 2
    manager.unreserve(2)
    assert manager.reserve() == 2
    assert manager.reserve() == 3
    assert manager.reserve() == 4
    assert manager.reserve() == 5
    manager.unreserve(5)

    manager = SeatManager(4)
    assert manager.reserve() == 1
    manager.unreserve(1)
    assert manager.reserve() == 1
    assert manager.reserve() == 2
    assert manager.reserve() == 3
    manager.unreserve(2)
    assert manager.reserve() == 2
    manager.unreserve(1)
    assert manager.reserve() == 1
    manager.unreserve(2)
