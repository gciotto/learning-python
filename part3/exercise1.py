S = 'string to be computed'

total = 0;

L = [];

for char in S:
    code = ord(char)
    print (code)
    total += code
    L.append(code)
    
print ('\nTotal count: %d' % total)
print (L)
