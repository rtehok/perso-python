class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = 0
        self.arr = [homepage]

    def visit(self, url: str) -> None:
        self.current += 1
        self.arr = self.arr[:self.current]
        self.arr.append(url)

    def back(self, steps: int) -> str:
        self.current = max(self.current - steps, 0)
        return self.arr[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.current + steps, len(self.arr) - 1)
        return self.arr[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

if __name__ == "__main__":
    obj = BrowserHistory("leetcode.com")
    obj.visit("google.com")
    obj.visit("facebook.com")
    obj.visit("youtube.com")
    print(obj.back(1))
    print(obj.back(1))
    print(obj.forward(1))
    obj.visit("linkedin.com")
    print(obj.forward(2))
    print(obj.back(2))
    print(obj.back(7))
