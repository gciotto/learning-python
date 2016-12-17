class Animal ():
    
    def reply (self):
        return self.speak()
    
    def speak (self):
        return None
        
class Mammal (Animal) : pass

class Cat (Mammal):
    
    def speak (self): return 'Meeeeeow'
    
class Dog (Mammal):
    
    def speak (self): return 'Aaaoooo'
    
class Primate (Mammal):
    
    def speak (self): return 'Hello World!'

class Hacker (Primate): pass

if __name__ == '__main__':

    h = Hacker()
    print (h.reply())
    
    c = Cat ()
    print (c.reply())
    
    d = Dog()
    print (d.reply())
    
    print (c.__class__ is Cat)