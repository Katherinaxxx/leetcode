class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.smin = []

    def push(self, x: int) -> None:
        self.s.append(x)
        if self.smin == [] or x <= self.smin[-1]:
            self.smin.append(x)

    def pop(self) -> None:
        if self.smin and self.s[-1] == self.smin[-1]:
            self.smin.pop()
        self.s.pop()

    def top(self) -> int:
        if self.s:
            return self.s[-1]

    def getMin(self) -> int:
        if self.smin:
            return self.smin[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()