class LinkedList:
    
    def __init__(self):
        self.l=[]
        
    
    def get(self, index: int) -> int:
        if 0 <=index <len(self.l):
            c=self.l[index]
            return c
        else:
            return -1
    def insertHead(self, val: int) -> None:
        self.l.insert(0,val)


    def insertTail(self, val: int) -> None:
        self.l.append(val)

    def remove(self, index: int) -> bool:
        if 0 <=index < len(self.l):
            self.l.pop(index)
            return True
        else:
            return False
        
    def getValues(self) -> List[int]:
        s=[]
        for b in self.l:
           s.append(b) 
        return s
        
