class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x) 
    # adds to top of stack (end of queue)

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            p = self.queue.pop()
            self.queue.append(p)
        return self.queue.pop()
    # removes the end of the queue
    # need to pop from the beginning and append the element popped, back to the end of the queue; cycle through for the length of the queue

    def top(self) -> int:
        return self.queue[-1]
    # top of stack = end of queue; use negative index to work backwards of the queue

    def empty(self) -> bool:
        if (len(self.queue) == 0):
            return True
        return False
    # checks the length of the queue, if its 0, its empty



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()