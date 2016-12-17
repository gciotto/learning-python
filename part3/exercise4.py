L = []

for i in range (0,10):
    L.append(2 ** i)
    
X = 5

if 2**X in L :
    print ('at index ' + str(L.index(2 ** X)))   
else: 
    print (str(X) + ' not found')
