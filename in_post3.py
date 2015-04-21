import stack
def in_post(expr):
   dic={}
   dic["*"]=3
   dic["/"]=3
   dic["+"]=2
   dic["-"]=2
   dic["("]=1
   op_stack=Stack()
   postfix=[]
   token=expr.split()
   for i in token:
