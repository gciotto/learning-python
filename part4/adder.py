def adder (*args, **kargs):  
    res = None
    
    if len (args) > 0:
        res = args[0]
        for x in args[1:]:
            res += x
    
    if len (kargs) > 0:
        
        keys = list(kargs.keys());
        
        if res == None: res = kargs[keys[0]]
        else: res += kargs[keys[0]]
        
        for key in keys [1:]:
            res += kargs[key]
    
    return res
        

print (adder (1, 2, a = 3, b= 3 ))
print (adder ("1", " + 2", x= " we", y= ' dasda'))
print (adder ([5, {'a': 2}], [1, 'coco']))

    