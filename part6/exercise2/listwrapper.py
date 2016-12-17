class Mylist():
    
    def __init__ (self, data = []):
        
        self.data = []
        
        for item in data:
            self.data.append(item)
    
    def __add__ (self, other):
        
        if type (other) == Mylist :
            return Mylist(self.data + other.data)
         
        return Mylist(self.data + other)
    
    def __mul__ (self, other):
        return Mylist(self.data * other)
    
    def __getitem__ (self, index):
        return self.data[index]
    
    def __len__ (self):
        return len (self.data)
    
    def __getslice__ (self, start, end):
        return Mylist(self.data [start:end])
    
    def append (self, data):
        self.data.append(data)
        
    def __repr__ (self):
        return "%s" % self.data
    
if __name__ == '__main__':
    
    x = Mylist ([1, 2, 4])
    
    print (x + [2, 3, 5])
    print ((x * 8), (x * 8)[4])
    print ((x * 8)[4:7])
    print (x + Mylist([111, 88, 99]))
    
    print (Mylist (Mylist ([2, 3 , 99])))
    
        