#stack operations functions are __init__,is_empty

class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)


s=stack()
s.push(5)
s.push(7)
print s
print s.pop()
