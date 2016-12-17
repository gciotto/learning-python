class Customer ():
    
    def line (self): print ('Customer method')
    
class Clerk () :
    
    def line (self): print ('Clerk method')

class Parrot () :
    
    def line (self): print ('Parrot method')
    
class Scene ():
    
    def __init__ (self):
        
        self.customer = Customer ()
        self.parrot = Parrot ()
        self.clerk = Clerk ()
        
    def action (self):
        
        self.customer.line()
        self.clerk.line()
        self.parrot.line()
        
        
if __name__ == '__main__':
    
    Scene().action()