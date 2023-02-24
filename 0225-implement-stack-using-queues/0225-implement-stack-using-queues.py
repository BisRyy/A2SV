class MyStack:

    def __init__(self):
        self.a = []
        self.size = 0

    def push(self, x: int) -> None:
        self.a.append(x)
        self.size+=1

    def pop(self) -> int:
        x = self.a[self.size-1]
        del self.a[self.size-1]
        self.size-=1
        return x

    def top(self) -> int:
        return self.a[self.size-1]
        

    def empty(self) -> bool:
        return self.size < 1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()