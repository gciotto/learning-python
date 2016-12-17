def copyDict(dict_arg):
    
    copy = {}
    
    for key in dict_arg:
        copy[key] = dict_arg[key]
        
    return copy

def addDict(dict_arg1, dict_arg2):
    
    if type (dict_arg1) == list and type (dict_arg2) == list:
        return dict_arg1 + dict_arg2
        
    res = {}
    
    for key in dict_arg1:
        res[key] = dict_arg1[key]
        
    for key in dict_arg2:
        if key not in dict_arg1:
            res[key] = dict_arg2[key]
        else: res[key] += dict_arg2[key] 
    
    return res

print (copyDict({'a': 2, 'b': 3}))
print (addDict({'a': 2, 'b': 3}, {'a':20, 'c': 4}))
print (addDict([1, 2], [3, 4]))

