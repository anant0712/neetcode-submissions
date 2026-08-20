class MinStack:

    def __init__(self):
        self.stack = []
            
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            previous_min = self.stack[-1][1]
            current_min = min(val,previous_min)
            self.stack.append((val,current_min))
        

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

        
