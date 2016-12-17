class Adder():
    
    def __init__ (self, data = []):
        self.data = data        
    
    def add (self, y):
        print ("Not Implemented")
        
    def __add__ (self, other):
        return self.add(other)
        
class ListAdder (Adder):
    
    def add (self, y):
        return self.data + y
    
class DictAdder (Adder):
    
    def add (self, y):
        res = {}
        
        for keys in self.data.keys(): 
            res [keys] = self.data[keys]
        
        for keys in y.keys():
            if y[keys] not in res:
                res [keys] = y [keys]
                
        return res
    

if __name__ == '__main__':
    a = Adder()
    a.add([1, 2, 3])
    
    b = ListAdder ([1, 2, 4])
    print (b + [5, 3, 1])
    
    c = DictAdder ({'a':a, 'b':b})
    print (c + {'c':'c'})
    
    
    

