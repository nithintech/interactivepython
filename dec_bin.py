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

#function for decimel to binary convertion using class stack
x=int(raw_input("enter a decimel number"))
def dec_bin(x):
    s=stack()
    dec_no=x
    while dec_no>0:
        rem=dec_no%2
        s.push(rem)
        dec_no=dec_no//2
    bin_str=""
    while not s.is_empty():
        bin_str=bin_str+str(s.pop())
    return "the binary equivalent of %d is %s\n"%(x,bin_str)
print dec_bin(x)
