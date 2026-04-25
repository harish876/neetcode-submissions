class MinStack:

    def __init__(self):
        self.stack = []
        self.mono_stack = [] # priority queue

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.mono_stack,val) # min heap
        
    def pop(self) -> None:
        """
        
        -3
        -2
        -2
        """
        removed = self.stack.pop()
        remove = True
        tmp = []
        for val in self.mono_stack:
            if remove and val == removed:
                remove = False
                continue
            heapq.heappush(tmp,val)

        self.mono_stack = tmp

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mono_stack[0] if len(self.mono_stack) else -1
