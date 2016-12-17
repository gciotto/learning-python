class Meta ():
    
    def __getattr__ (self, name):
        print ('Get ', name)
        return self.__dict__[name]
    
    def __setattr__ (self, name, value):
        print ('Set ', name, value)
        self.__dict__[name] = value
        

if __name__ == '__main__':
    
    x = Meta()
    x.v1 = 1
    x.v23 = [2, 3]
    
    a = x.v1