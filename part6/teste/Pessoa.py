'''
Created on Jan 15, 2016

@author: gciotto
'''
class Pessoa():
 
    number_of_instances = 0;
    
    x = 'coco'

    def __init__(self, idade, nome = 'Joao',  sexo = 'M'):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        
        Pessoa.number_of_instances += 1
    
    def __add__ (self, other):
        return self.idade + other.idade
        
class MonstroSagrado (Pessoa):
    
    number_of_instances = 0
    
    def __init__ (self, conquista, idade, nome, sexo):
        Pessoa.__init__(self, idade, nome, sexo)
        self.conquista = conquista
        
        MonstroSagrado.number_of_instances += 1
    
    def getNumberOfInstances():
        return MonstroSagrado.number_of_instances
    
    getNumberOfInstances = staticmethod (getNumberOfInstances)
    
    def __str__ (self):
        return 'Conquista "%s" realizada pelo monstro sagrado chamado %s' % (self.conquista, self.nome)

p1 = Pessoa(22, 'Gugu',  'M')
p2 = Pessoa(21)

eu = MonstroSagrado('ser lindo', 22, 'Gustavo', 'M')

print (eu.__class__.__bases__[0].__name__, p1.__class__.__name__)

print (p1.x, p2.x, Pessoa.x, p1 + p2)
print (eu)
print (dir(eu))
print (eu.__dict__)
print (MonstroSagrado.number_of_instances, MonstroSagrado.getNumberOfInstances(), Pessoa.number_of_instances)