# Learning Python - Part I - Exercise 2
string = input('Type in an expression: ')

print(string + '2', type (string), int(string) + 2) 

if type(int(string)) != str:
    print('coco') 

I = [[[ 1, 2, 3 ], [4, 5, 6]] ,[[ 1, 2, 3 ], [4, 5, 6]], [[ 1, 2, 3 ], [4, 5, 6]]]
print(I[0], I[1], I[2])

print ([[(x+y+z)/3 for x in I[0] for y in I[1] for z in I[2]]])