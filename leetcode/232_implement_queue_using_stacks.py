from collections import deque


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

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
