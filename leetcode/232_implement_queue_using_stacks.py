class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        while len(self.stack_in):
            top = self.stack_in.pop()
            self.stack_out.append(top)
        self.stack_in.append(x)
        while len(self.stack_out):
            top = self.stack_out.pop()
            self.stack_in.append(top)

    def pop(self) -> int:
        return self.stack_in.pop()

    def peek(self) -> int:
        return self.stack_in[-1]

    def empty(self) -> bool:
        return not len(self.stack_in)


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert not q.empty()
