class MinStack:

    def __init__(self):
        self.l=[]

    def push(self, val: int) -> None:
        self.l.append(val)

    def pop(self) -> None:
        if(len(self.l)==0):
            return -1
        self.l.pop(-1)

    def top(self) -> int:
        if(len(self.l)==0):
            return -1
        return self.l[-1]

    def getMin(self) -> int:
        m=10000000000000000000000000000000000
        for i in self.l:
            if(i<m):
                m=i
            
        return m
            
