import bisect
import collections


class SnapshotArray:

    def __init__(self, length: int):
        self.history_records = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.history_records[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.history_records[index],
                                         [snap_id, 10 ** 9])
        return self.history_records[index][snap_index - 1][1]


if __name__ == "__main__":
    obj = SnapshotArray(3)
    obj.set(0, 5)
    assert obj.snap() == 0
    obj.set(0, 6)
    assert obj.get(0, 0) == 5

    sn = SnapshotArray(3)
    sn.set(0, 4)
    sn.set(0, 16)
    sn.set(0, 13)
    assert sn.snap() == 0
    assert sn.get(0, 0) == 13
    assert sn.snap() == 1
