class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.data = []

    def push(self, x: int) -> None:
        if len(self.data) < self.maxSize:
            self.data.append(x)

    def pop(self) -> int:
        return self.data.pop() if len(self.data) != 0 else -1


    def increment(self, k: int, val: int) -> None:
        mn = min(len(self.data), k)
        for i in range(mn):
            self.data[i] += val