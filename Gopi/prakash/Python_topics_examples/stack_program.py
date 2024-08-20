class stack:

    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):

        return self.items[-1]

    def size(self):

        return len(self.items)

my_stack=stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

print(my_stack.size())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.size())

print("-----------------------------------------------------------------")

class Stack:

    def __init__(self):

        self.items=[]

    def is_empty(self):
        return self.items == []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

obj_stack= Stack()

"""
obj_stack.push(1)
obj_stack.push(2)
obj_stack.push(3)
obj_stack.push(4)
"""

print(obj_stack.size())
print(obj_stack.peek())
print(obj_stack.pop())
print(obj_stack.size())


        
            
    
    

    
        
