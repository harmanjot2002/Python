iterable_value="Pantech"
iterable_obj=iter(iterable_value)

while True:
    try:
        #Iterate by calling next
        item=next(iterable_obj)
        print(item)
    except:
        #exception will happen when iteration will over
        break
    
class Test:
    #constructor
    def __init__(self,limit):
        self.limit=limit
    
    #creates iterator object
    #called when iterator is initiated
    def __iter__(self):
        self.x=10
        return self
    
    #To move to next element.In python3,we should replace with __next__
    def __next__(self):
        x=self.x
        
        if x>self.limit:
            raise StopIteration
            
        self.x=x+1;
        return x

for i in Test(15):
    print(i)
    
for i in Test(5):
    print (i)

from math import sqrt,factorial
print(sqrt(25))
print(factorial(5)) 