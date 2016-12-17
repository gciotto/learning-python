from exercise2.listwrapper import Mylist

class MylistSub (Mylist):
    
    number_of_calls = 0
    
    def __init__ (self, data = []):
        MylistSub.number_of_calls += 1
        Mylist.__init__(self, data)
    
    def __add__ (self, other):
        MylistSub.number_of_calls += 1    
        
        if type (other) == MylistSub:
            return MylistSub(self.data + other.data) 
            
        return MylistSub(Mylist.__add__(self, other))
    
    def __mul__ (self, other):
        MylistSub.number_of_calls += 1
        return MylistSub(Mylist.__mul__(self, other))
    
    def __getitem__ (self, index):
        MylistSub.number_of_calls += 1
        return Mylist.__getitem__(self, index)
    
    def __len__ (self):
        MylistSub.number_of_calls += 1
        return Mylist.__len__(self)
    
    def __getslice__ (self, start, end):
        MylistSub.number_of_calls += 1
        return Mylist.__getslice__(self, start, end)
    
    def append (self, data):
        MylistSub.number_of_calls += 1
        Mylist.append(self, data)
        
    def __repr__ (self):
        MylistSub.number_of_calls += 1
        return Mylist.__repr__(self)

    def getNumberOfCalls ():
        return MylistSub.number_of_calls
    getNumberOfCalls = staticmethod (getNumberOfCalls)
    
if __name__ == '__main__':
    
    x = MylistSub ([1, 2, 3])
    
    print (x + [2, 3, 5])
    print ((x * 8), (x * 8)[4])
    print ((x * 8)[4:7])
    print (x + MylistSub([111, 88, 99]))
    print (MylistSub (MylistSub ([2, 3 , 99])))
    print (MylistSub.getNumberOfCalls())