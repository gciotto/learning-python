class Lunch ():
    
    def __init__ (self): 
        self.customer = Customer()
        self.employee = Employee ()
         
    def order (self, foodName):
        self.customer.placeOrder(foodName, self.employee)
        
    def result (self): return self.customer.printFood()
    
class Customer ():
    
    def __init__ (self):
        self.food = None
        
    def placeOrder (self, foodName, employee):
        self.food = employee.takeOrder(foodName)
        
    def printFood (self): return self.food

class Employee ():
    
    def takeOrder (self, foodName): return Food (foodName)

class Food ():
    
    def __init__ (self, name): 
        self.name = name
        
    def getFoodName (self): return self.name
    

if __name__ == '__main__':
    l = Lunch()
    
    l.order('coco frito')
    
    print (l.result().getFoodName())