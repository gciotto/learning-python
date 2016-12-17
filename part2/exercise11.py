file = open('file11.txt', 'w')
file.write ('hello file world!\n')
file.close()

fileRead = open('file11.txt', 'r')
print (fileRead.readline())
fileRead.close()
