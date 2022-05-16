import math

a = 42

c = 42
def butoma(x, y):
    return math.sin(c * x * y)

def recusia(n):
    if n == 1:
        return 1
    return 1 + 2*recusia(n-1)

class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_count(self):
        print('All amount of Employess: %d' % 15)



class Tree(object):
    def __init__(self, kind, height):
        self.kind = kind
        self.age = 0
        self.height = height
 
    def info(self):
        print ("{} years old {}. {} meters high.".format(self.age, self.kind, self.height))    
 
    def grow(self):
        self.age += 1
        self.height += 0.5

class FruitTree(Tree):
    def food(self):
        print('I want a lot of coffee')

vasya = Employee('Vasya',42)