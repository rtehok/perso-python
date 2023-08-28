import collections


class MyStack:

    def __init__(self):
        # self.q = []
        self.q = collections.deque()

    def push(self, x: int) -> None:
        # self.q.append(x)
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.pop())

    def pop(self) -> int:
        # return self.q.pop()
        return self.q.popleft()

    def top(self) -> int:
        # return self.q[-1]
        return self.q[0]

    def empty(self) -> bool:
        # return len(self.q) == 0
        return len(self.q) == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    assert obj.top() == 2
    assert obj.pop() == 2
    assert not obj.empty()
