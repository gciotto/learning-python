class Set():
    
    def __init__ (self, value = []):
        self.data = []
        self.concat(value)
        
    def intersect (self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        
        return Set(res)
    
    def union (self, other):
        
        res = self.data[:]
        for x in other: 
            if x not in res:
                res.append(x)
            
        return Set(res)
    
    def concat (self, value):
        
        for x in value:
            if x not in self.data:
                self.data.append(x)
                
    def __len__(self): return len (self.data)
    def __getitem__ (self, index): return self.data[index]
    def __and__ (self, other): return self.intersect(other)
    def __or__ (self,other): return self.union(other)
    def __repr__ (self): return 'Set: ' + str(self.data)
                

class SetSub (Set):
    
    def __init__ (self, *args):
        self.data = []
        for x in args:
            self.concat(x)
    
    def intersect(self, *others):
        res = []
        
        for x in self.data: 
            for y in others:
                if x not in y:
                    break
            else: res.append(x)
        
        return SetSub (res)
    
    def union (self, *others):
        
        res = SetSub(self.data)
        
        for x in others:
            res = SetSub(Set.union(res, x))
        
        return res

if __name__ == '__main__':
    s1 = Set ([1, 5, 55])
    s2 = Set ([1, 4444, 55])
    
    print (s1 | s2, s1 & s2)
    
    s3 = Set ('tricolor')
    s4 = Set ('trico')
    print (s3, s4 & s3, s3 & 'coco', s4 | 'xopo')
    
    s5 = SetSub (s1, s3)
    print (s5)
    print (s5.union(s1, s2, s3), s5.intersect(s1, s2, s3))
    