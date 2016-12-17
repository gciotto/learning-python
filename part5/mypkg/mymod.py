def countLines(name):
    
    file = open(name, 'r')
    res =  len(file.readlines())
    file.close()
    return res

def countChars(name):
    
    file = open(name, 'r')
    res = len(file.read())
    file.close()
    return res

def test (name):
    
    return countLines(name), countChars(name)

if __name__ == "__main__":
    print (test("mymod.py"))
         
